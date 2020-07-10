#!/usr/bin/env python3

import csv

def emacsify(rows):
	output_text = ''

	for row in rows:
		output_text += f'* {row["name"]}\n'
		if row["detail"] != '':
			output_text += f'{row["detail"]}\n'

	return output_text

def main():
	csv_reader = ''
	selected_rows = []

	with open('./elements.csv') as csv_file:
		csv_reader = csv.DictReader(csv_file, delimiter=',')
		for row in csv_reader:
			selected_rows.append(row)

	formatted_output = emacsify(selected_rows)
	print(formatted_output)

	with open('./todays_routine.org', 'w') as file:
		file.write(formatted_output)

main()