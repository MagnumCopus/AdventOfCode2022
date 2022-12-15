
# Project: 	Advent of Code 2022 - Day 15
# Author: 	Jake Cope
# Date:		12/15/2022

import time
import math

input_file = "input/day15.txt"
inputs = []
with open(input_file, "r") as file:
	inputs = file.read().splitlines() 

start_time = time.time()

# ********************************
# *            PART 1            *
# ********************************

print("\n*** Part 1 ***")

y_slice = 2000000
impossible_x_ranges = []
for i in range(len(inputs)):
	command = inputs[i].split(' ')
	sensor_x = int(command[2][2:-1])
	sensor_y = int(command[3][2:-1])
	beacon_x = int(command[8][2:-1])
	beacon_y = int(command[9][2:])
	dist_to_beacon = abs(sensor_y - beacon_y) + abs(sensor_x - beacon_x)
	if abs(sensor_y - y_slice) <= dist_to_beacon:
		left_intersect = -dist_to_beacon + abs(sensor_y - y_slice) + sensor_x
		right_intersect = dist_to_beacon - abs(sensor_y - y_slice) + sensor_x
		impossible_x_ranges.append([left_intersect, right_intersect])

impossible_x_ranges.sort(key = lambda x_range : x_range[0])

not_possible_count = 0
processing = impossible_x_ranges[0][0]-1
for i in range(len(impossible_x_ranges)):
	if impossible_x_ranges[i][0] > processing:
		processing = impossible_x_ranges[i][0]
	if impossible_x_ranges[i][1] > processing:
		not_possible_count += impossible_x_ranges[i][1] - processing
		processing = impossible_x_ranges[i][1]

print(not_possible_count)


# ********************************
# *            PART 2            *
# ********************************

print("\n*** Part 2 ***")

bound = 4000000
impossible_x_ranges = [[] for y_slice in range(bound+1)]
for i in range(len(inputs)):
	command = inputs[i].split(' ')
	sensor_x = int(command[2][2:-1])
	sensor_y = int(command[3][2:-1])
	beacon_x = int(command[8][2:-1])
	beacon_y = int(command[9][2:])
	dist_to_beacon = abs(sensor_y - beacon_y) + abs(sensor_x - beacon_x)
	for y_slice in range(sensor_y-dist_to_beacon, sensor_y+dist_to_beacon+1):
		if y_slice < 0:
			continue
		elif y_slice > bound:
			break
		left_intersect = -dist_to_beacon + abs(sensor_y - y_slice) + sensor_x
		right_intersect = dist_to_beacon - abs(sensor_y - y_slice) + sensor_x
		impossible_x_ranges[y_slice].append([left_intersect, right_intersect])

for row in impossible_x_ranges:
	row.sort(key = lambda x_range : x_range[0])

for y in range(len(impossible_x_ranges)):
	processing = 0
	found_hole = False
	for x in range(len(impossible_x_ranges[y])):
		if impossible_x_ranges[y][x][0] > processing:
			print((impossible_x_ranges[y][x][0]-1) * 4000000 + y)
			found_hole = True
			break
		if impossible_x_ranges[y][x][1] > bound:
			break
		if impossible_x_ranges[y][x][1] > processing:
			processing = impossible_x_ranges[y][x][1]
	if found_hole:
		break


end_time = time.time()
time_lapsed = end_time - start_time
print("\nTime elapsed: {0} seconds".format(round(time_lapsed, 5))) 	