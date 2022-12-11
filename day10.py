
# Project: 	Advent of Code 2022 - Day 10
# Author: 	Jake Cope
# Date:		12/10/2022

import time

input_file = "input/day10.txt"
inputs = []
with open(input_file, "r") as file:
	inputs = file.read().splitlines() 

start_time = time.time()

# ********************************
# *            PART 1            *
# ********************************

print("\n*** Part 1 ***")

signal_sum = 0
cycle_count = 0
register = 1
def cycle_part1():
	global signal_sum
	global cycle_count
	cycle_count += 1
	if (cycle_count - 20) % 40 == 0:
		signal_sum += register * cycle_count

for i in range(0, len(inputs)):
	if inputs[i][0:4] == 'noop':
		cycle_part1()
	else:
		cycle_part1()
		cycle_part1()
		register += int(inputs[i][5:])

print(signal_sum)


# ********************************
# *            PART 2            *
# ********************************

print("\n*** Part 2 ***")

cycle_count = 0
register = 1
def cycle_part2():
	global cycle_count
	cycle_count += 1
	if abs(((cycle_count - 1) % 40) - register) <= 1:
		print('#', end = '')
	else:
		print('.', end = '')
	if cycle_count % 40 == 0:
		print()

for i in range(0, len(inputs)):
	if inputs[i][0:4] == 'noop':
		cycle_part2()
	else:
		cycle_part2()
		cycle_part2()
		register += int(inputs[i][5:])

end_time = time.time()
time_lapsed = end_time - start_time
print("\nTime elapsed: {0} seconds".format(round(time_lapsed, 5))) 	