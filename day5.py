
# Project: 	Advent of Code 2022 - Day 5
# Author: 	Jake Cope
# Date:		12/05/2022

import time

input_file = "input/day5.txt"
inputs = []
with open(input_file, "r") as file:
	inputs = file.readlines()

start_time = time.time()

# ********************************
# *            PART 1            *
# ********************************

print("\n*** Part 1 ***")

bottom_row_line = 7
stack_num = 9
stacks = []
for i in range(0, stack_num):
	stacks.append([])
for row in range(bottom_row_line, -1, -1):
	for i in range(0, stack_num):
		cursor = i*4
		crate = inputs[row][cursor:cursor+4].strip()[1:2]
		if crate != '':
			stacks[i].append(crate)

for i in range(bottom_row_line+3, len(inputs)):
	commands = inputs[i].split(' ')
	num_crates = int(commands[1])
	from_stack = int(commands[3])-1
	to_stack = int(commands[5])-1
	for crate in range(0, num_crates):
		stacks[to_stack].append(stacks[from_stack].pop())

tops = ''
for i in range(0, stack_num):
	tops += stacks[i].pop()
print(tops)


# ********************************
# *            PART 2            *
# ********************************

print("\n*** Part 2 ***")

bottom_row_line = 7
stack_num = 9
stacks = []
for i in range(0, stack_num):
	stacks.append([])
for row in range(bottom_row_line, -1, -1):
	for i in range(0, stack_num):
		cursor = i*4
		crate = inputs[row][cursor:cursor+4].strip()[1:2]
		if crate != '':
			stacks[i].append(crate)

for i in range(bottom_row_line+3, len(inputs)):
	commands = inputs[i].split(' ')
	num_crates = int(commands[1])
	from_stack = int(commands[3])-1
	to_stack = int(commands[5])-1
	temp_stack = []
	for crate in range(0, num_crates):
		if len(stacks[from_stack]) > 0:
			temp_stack.append(stacks[from_stack].pop())
	for crate in range(0, len(temp_stack)):
		stacks[to_stack].append(temp_stack.pop())

tops = ''
for i in range(0, stack_num):
	tops += stacks[i].pop()
print(tops)


end_time = time.time()
time_lapsed = end_time - start_time
print("\nTime elapsed: {0} seconds".format(round(time_lapsed, 5)))