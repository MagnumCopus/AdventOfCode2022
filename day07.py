
# Project: 	Advent of Code 2022 - Day 7
# Author: 	Jake Cope
# Date:		12/07/2022

import time

input_file = "input/day7.txt"
inputs = []
with open(input_file, "r") as file:
	inputs = file.readlines()

start_time = time.time()

# ********************************
# *            PART 1            *
# ********************************

print("\n*** Part 1 ***")

directory_sizes = {}
path_stack = []

for i in range(0, len(inputs)):
	line = inputs[i].strip()
	if line[0] == '$':
		cmd = line[2:]
		if cmd[0:2] == 'cd':
			if line[5:] == '/':
				path_stack = ['/']
			elif line[5:] == '..':
				path_stack.pop()
			else:
				path_stack.append(line[5:])
	elif line[0:4] == 'dir ':
		continue;
	else:
		file = line.split(' ')
		size = int(file[0])
		name = file[1]
		for i in range(len(path_stack), 0, -1):
			path = '/'.join(path_stack[:i])
			if path not in directory_sizes.keys():
				directory_sizes[path] = 0
			directory_sizes[path] += size;

total = 0
for k in directory_sizes.keys():
	if directory_sizes[k] <= 100000:
		total += directory_sizes[k]
print(total)


# ********************************
# *            PART 2            *
# ********************************

print("\n*** Part 2 ***")

space_left = 70000000 - directory_sizes['/']
space_needed = 30000000 - space_left
min_size = 70000000
for k in directory_sizes.keys():
	if directory_sizes[k] >= space_needed and directory_sizes[k] < min_size:
		min_size = directory_sizes[k]
print(min_size)


end_time = time.time()
time_lapsed = end_time - start_time
print("\nTime elapsed: {0} seconds".format(round(time_lapsed, 5)))