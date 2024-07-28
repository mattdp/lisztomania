#!/usr/bin/env python3

import os
from task import Task

# import Instructions from sample_input in replicable way. assumes directory is there.
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), 'sample_inputs'))
from instructions import Instructions

"""
TODO: tag-based screening
    TODO: screen for a particular tag only
    TODO: respect depth - should probably carry upper layer's tags with a task so they can be nested
        DONE: change on depth
        TODO: add tags as encounter Tasks
        TODO: check present and higher level tags as go along
TODO: probability and randomness, likely TaskSet where none or some tasks picked
TODO: exercise, personal time removed - put in personal CL
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
    accrued_tags = {}
    accrued_tags[1] = []
    
    current_depth = default_depth
    instructions = Instructions.instructions_list()

    screened_out_tags = ["work"]
    required_tags = [""]

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
            if i.tags:
                tag_set = set(i.tags)
                if screened_out_tags and tag_set.intersection(screened_out_tags):
                    continue #if any screened out tags present, skip this element

            formatted_output += "*"*current_depth + " " + i.title
            if i.note:
                formatted_output += "\n"+i.note
            formatted_output += "\n"

    if debug:
        print(formatted_output)
    
    with open(write_path, 'w') as file:
        file.write(formatted_output)

main()