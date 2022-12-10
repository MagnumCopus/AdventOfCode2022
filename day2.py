
# Project: 	Advent of Code 2022 - Day 2
# Author: 	Jake Cope
# Date:		12/02/2022

import time

input_file = "input/day2.txt"
inputs = []
with open(input_file, "r") as file:
	inputs = file.readlines()

start_time = time.time()

# ********************************
# *            PART 1            *
# ********************************

print("\n*** Part 1 ***")

score = 0
for i in range(0, len(inputs)):
	guide = inputs[i].split()
	elf_move = guide[0]
	my_move = guide[1]

	if my_move == 'X':
		score += 1
	elif my_move == 'Y':
		score += 2
	elif my_move == 'Z':
		score += 3

	if elf_move == 'A':
		if my_move == 'X':
			score += 3
		elif my_move == 'Y':
			score += 6
	elif elf_move == 'B':
		if my_move == 'Y':
			score += 3
		elif my_move == 'Z':
			score += 6
	elif elf_move == 'C':
		if my_move == 'Z':
			score += 3
		elif my_move == 'X':
			score += 6
print(score)


# ********************************
# *            PART 2            *
# ********************************

print("\n*** Part 2 ***")

score = 0
for i in range(0, len(inputs)):
	guide = inputs[i].split()
	elf_move = guide[0]
	outcome = guide[1]

	if outcome == 'Y':
		score += 3
	elif outcome == 'Z':
		score += 6

	if elf_move == 'A':
		if outcome == 'X':
			score += 3
		elif outcome == 'Y':
			score += 1
		else:
			score += 2
	elif elf_move == 'B':
		if outcome == 'X':
			score += 1
		elif outcome == 'Y':
			score += 2
		else:
			score += 3
	elif elf_move == 'C':
		if outcome == 'X':
			score += 2
		elif outcome == 'Y':
			score += 3
		else:
			score += 1
print(score)


end_time = time.time()
time_lapsed = end_time - start_time
print("\nTime elapsed: {0} seconds".format(round(time_lapsed, 5)))