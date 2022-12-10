
# Project: 	Advent of Code 2022 - Day 1
# Author: 	Jake Cope
# Date:		12/01/2022

import time

input_file = "input/day1.txt"
inputs = []
with open(input_file, "r") as file:
	inputs = file.readlines()

start_time = time.time()

# ********************************
# *            PART 1            *
# ********************************

print("\n*** Part 1 ***")

elf_calories = [0]
for i in range(0, len(inputs)):
	if inputs[i] != '\n':
		elf_calories[-1] += int(inputs[i])
	else:
		elf_calories.append(0)
sorted_calories = sorted(elf_calories, reverse=True)
print(sorted_calories[0])


# ********************************
# *            PART 2            *
# ********************************

print("\n*** Part 2 ***")

print(sum(sorted_calories[0:3]))


end_time = time.time()
time_lapsed = end_time - start_time
print("\nTime elapsed: {0} seconds".format(round(time_lapsed, 5)))