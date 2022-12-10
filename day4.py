
# Project: 	Advent of Code 2022 - Day 4
# Author: 	Jake Cope
# Date:		12/04/2022

import time

input_file = "input/day4.txt"
inputs = []
with open(input_file, "r") as file:
	inputs = file.readlines()

start_time = time.time()

# ********************************
# *            PART 1            *
# ********************************

print("\n*** Part 1 ***")

count = 0
for i in range(0, len(inputs)):
	pair = inputs[i].split(',')
	edges1 = pair[0].split('-')
	edges2 = pair[1].split('-')
	sections1 = range(int(edges1[0]), int(edges1[1])+1)
	sections2 = range(int(edges2[0]), int(edges2[1])+1)
	subset1 = True
	subset2 = True
	for section in sections1:
		if section not in sections2:
			subset1 = False
			break;
	for section in sections2:
		if section not in sections1:
			subset2 = False
			break;
	if subset1 or subset2:
		count += 1
print(count)

# ********************************
# *            PART 2            *
# ********************************

print("\n*** Part 2 ***")

count = 0
for i in range(0, len(inputs)):
	pair = inputs[i].split(',')
	edges1 = pair[0].split('-')
	edges2 = pair[1].split('-')
	sections1 = range(int(edges1[0]), int(edges1[1])+1)
	sections2 = range(int(edges2[0]), int(edges2[1])+1)
	for section in sections1:
		if section in sections2:
			count += 1
			break;
print(count)


end_time = time.time()
time_lapsed = end_time - start_time
print("\nTime elapsed: {0} seconds".format(round(time_lapsed, 5)))