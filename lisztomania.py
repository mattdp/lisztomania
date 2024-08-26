#!/usr/bin/env python3

import os
from task import Task

# import Instructions from sample_input in replicable way. assumes directory is there.
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), 'sample_inputs'))
from instructions import Instructions
from quotes import Quotes

"""
TODO: add some good personal tags to mix for a composite list
TODO: use for a while
TODO: probability and randomness, likely TaskSet where none or some tasks picked

TODO: exercise, personal time removed - put in personal CL
TODO: tag-based screening tests - tried simple cases, not confident of complex
"""

write_path_default_value = './todays_routine.org' 
write_path = os.getenv('LIZTOMANIA_WRITE_PATH',write_path_default_value)

INSTRUCTION_COMMANDS = [
    "DEPTH_DOWN", 
    "DEPTH_UP", 
    "DEPTH_DEFAULT",
]

def main():
    debug = True    
    default_depth = 1 #how many "*" to append to a top-level task
    formatted_output = ''
    accrued_tags = {} #storage by level of which tags apply
    accrued_tags[1] = []
    applicable_tags = [] #at moment of evaluation, all tags from all layers applying to context
    
    current_depth = default_depth
    instructions = Instructions.instructions_list()
    quotes = Quotes.get_quotes(2)

    screened_out_tags = []
    required_tags = [] 

    for q in range(0,len(quotes)):
        formatted_output += "\""+quotes[q][0]+"\" -"+quotes[q][1]+"\n"

    for i in instructions:
        if i == "DEPTH_DOWN":
            current_depth += 1
            if not(current_depth in accrued_tags):
                accrued_tags[current_depth] = []
        elif i == "DEPTH_UP":
            accrued_tags[current_depth] = [] 
            current_depth -= 1
        elif i == "DEPTH_DEFAULT":
            for key in accrued_tags:
                accrued_tags[key] = []
            current_depth = default_depth
        else: #it's a task
            accrued_tags[current_depth] = i.tags if i.tags else [] #tags thrown out each cycle unless they're at a higher level
            if screened_out_tags or required_tags:
                applicable_tags = []                    
                for key in accrued_tags:
                    values = accrued_tags[key]
                    for value in values:
                        applicable_tags.append(value)
                applicable_tag_set = set(applicable_tags)

                if screened_out_tags and applicable_tag_set.intersection(screened_out_tags):
                    continue #if any screened out tags present, skip this element
                if required_tags:
                    intersection = applicable_tag_set.intersection(required_tags)
                    if not all(element in intersection for element in required_tags): #unless all required tags present
                        continue

            formatted_output += "*"*current_depth + " " + i.title
            if i.note:
                formatted_output += "\n"+i.note
            formatted_output += "\n"

    if debug:
        print(formatted_output)
    
    with open(write_path, 'w') as file:
        file.write(formatted_output)

main()