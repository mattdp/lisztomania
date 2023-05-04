#!/usr/bin/env python3

import csv
import sys, getopt
import random

#assuming need ** prefix to paste into bigger file right now
def emacsify(rows,star_prefix = 2):

	output_text = ''

	categories = ["1. morning", "2. afternoon", "3. evening"]
	for category in categories:
		for i in range(star_prefix):
			output_text += "*"
		output_text += f" {category}\n"
		for row in rows:
			if row["timing"] == category:
				for i in range(star_prefix+1):
					output_text += "*"
				output_text += f' {row["name"]}\n'
				if row["detail"] != '':
					output_text += f'{row["detail"]}\n'

	return output_text

def parse_cli(argv):

	help_string = './composer.py\n-p <priority: ["red"|"yellow"|"green"]>\n-d <daytype: ["workday"|"weekend"]>'
	arguments = {}

	try:
		opts, args = getopt.getopt(argv,'hp:d:',['priority=','day_type='])
	except getopt.GetoptError:
		print(help_string)
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print(help_string)
			sys.exit()
		elif opt in ("-p", "--priority"):
			arguments["priority"] = arg
		elif opt in ("-d", "--daytype"):
			arguments["day_type"] = arg
	
	return arguments

#return T or F
#lets things through unless reason to remove
def row_test(row, arguments):
	debug = False
	if debug:
		print(f'row: {row}')
		print(f'args: {arguments}')
	#don't show work stuff on weekends
	if "day_type" in arguments and arguments["day_type"] == "weekend":
		if row["category"] == "work":
			return False
	#don't show non-urgent stuff on stressful days
	if "priority" in arguments:
		if arguments["priority"] == "red" and (row["priority"] in ["green", "yellow"]):
			return False
		elif arguments["priority"] == "yellow" and (row["priority"] == "green"):
			return False	
	return True

def main(argv):

	arguments = parse_cli(argv)
	debug = False
	formatted_output = ''

	csv_reader = ''
	quote_rows = []
	with open('./quotes.csv') as csv_file:
		csv_reader = csv.DictReader(csv_file, delimiter=',')
		for row in csv_reader:
			quote_rows.append(row)

	quote_count = len(quote_rows)
	selections = 2

	# can currently select the same quote multiple times/day
	for i in range(0,selections):
		selection_index = random.randint(0,quote_count-1)
		quote_row = quote_rows[selection_index]
		formatted_output += f'"{quote_row["Quote"]}" -{quote_row["Attribution"]}\n'

	csv_reader = ''
	action_rows_selected = []

	with open('./elements.csv') as csv_file:
		csv_reader = csv.DictReader(csv_file, delimiter=',')
		for row in csv_reader:
			if row_test(row, arguments):
				action_rows_selected.append(row)

	formatted_output += emacsify(action_rows_selected)
	if debug:
		print(formatted_output)

	with open('./todays_routine.org', 'w') as file:
		file.write(formatted_output)

# needed to actually run the program
main(sys.argv[1:])