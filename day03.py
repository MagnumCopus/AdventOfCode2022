
# Project: 	Advent of Code 2022 - Day 3
# Author: 	Jake Cope
# Date:		12/03/2022

import time

input_file = "input/day3.txt"
inputs = []
with open(input_file, "r") as file:
	inputs = file.readlines()

start_time = time.time()

# ********************************
# *            PART 1            *
# ********************************

print("\n*** Part 1 ***")

priorities = 0
for i in range(0, len(inputs)):
	line = inputs[i]
	num_badges = int(len(line) / 2)
	sack1 = line[:num_badges]
	sack2 = line[num_badges:]
	for badge in sack1:
		if badge in sack2:
			if (badge >= 'a'):
				priorities += ord(badge) - ord('a') + 1
			else:
				priorities += ord(badge) - ord('A') + 27
			break;
print(priorities)


# ********************************
# *            PART 2            *
# ********************************

print("\n*** Part 2 ***")

priorities = 0
for i in range(0, len(inputs), 3):
	sack1 = inputs[i]
	sack2 = inputs[i+1]
	sack3 = inputs[i+2]
	for badge in sack1:
		if badge in sack2 and badge in sack3:
			if (badge >= 'a'):
				priorities += ord(badge) - ord('a') + 1
			else:
				priorities += ord(badge) - ord('A') + 27
			break;
print(priorities)


end_time = time.time()
time_lapsed = end_time - start_time
print("\nTime elapsed: {0} seconds".format(round(time_lapsed, 5)))