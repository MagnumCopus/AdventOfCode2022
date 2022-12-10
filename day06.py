
# Project: 	Advent of Code 2022 - Day 6
# Author: 	Jake Cope
# Date:		12/06/2022

import time

input_file = "input/day6.txt"
inputs = []
with open(input_file, "r") as file:
	inputs = file.readlines()

start_time = time.time()

# ********************************
# *            PART 1            *
# ********************************

print("\n*** Part 1 ***")

signal = inputs[0]
for i in range(4, len(signal)):
	marker = set(signal[i-4:i])
	if len(marker) == 4:
		print(i)
		break


# ********************************
# *            PART 2            *
# ********************************

print("\n*** Part 2 ***")

signal = inputs[0]
for i in range(14, len(signal)):
	marker = set(signal[i-14:i])
	if len(marker) == 14:
		print(i)
		break


end_time = time.time()
time_lapsed = end_time - start_time
print("\nTime elapsed: {0} seconds".format(round(time_lapsed, 5)))