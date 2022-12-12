
# Project: 	Advent of Code 2022 - Day 12
# Author: 	Jake Cope
# Date:		12/12/2022

import time
import sys

input_file = "input/day12.txt"
inputs = []
with open(input_file, "r") as file:
	inputs = file.read().splitlines() 

start_time = time.time()

# ********************************
# *            PART 1            *
# ********************************

print("\n*** Part 1 ***")

distances = [[100000 for x in range(len(inputs[0]))] for i in range(len(inputs))]
def get_map_height(y, x):
	if y < 0 or y >= len(inputs) or x < 0 or x >= len(inputs[y]):
		return None
	height = inputs[y][x]
	if height == 'S':
		return 'a'
	elif height == 'E':
		return 'z'
	return height

start = [0,0]
goal = [0,0]
for i in range(len(inputs)):
	if 'S' in inputs[i]:
		start = [i, inputs[i].find('S')]
		distances[start[0]][start[1]] = 0
	if 'E' in inputs[i]:
		goal = [i, inputs[i].find('E')]

areas_to_check = [start]
while len(areas_to_check) > 0:
	area = areas_to_check.pop()
	height = get_map_height(area[0], area[1])
	current_distance = distances[area[0]][area[1]]
	
	up_height = get_map_height(area[0]-1, area[1])
	if up_height:
		up_distance = distances[area[0]-1][area[1]]
		if ord(up_height) - ord(height) <= 1 and current_distance + 1 < up_distance:
			distances[area[0]-1][area[1]] = current_distance + 1
			areas_to_check.append([area[0]-1, area[1]])

	right_height = get_map_height(area[0], area[1]+1)
	if right_height:
		right_distance = distances[area[0]][area[1]+1]
		if ord(right_height) - ord(height) <= 1 and current_distance + 1 < right_distance:
			distances[area[0]][area[1]+1] = current_distance + 1
			areas_to_check.append([area[0], area[1]+1])

	down_height = get_map_height(area[0]+1, area[1])
	if down_height:
		down_distance = distances[area[0]+1][area[1]]
		if ord(down_height) - ord(height) <= 1 and current_distance + 1 < down_distance:
			distances[area[0]+1][area[1]] = current_distance + 1
			areas_to_check.append([area[0]+1, area[1]])

	left_height = get_map_height(area[0], area[1]-1)
	if left_height:
		left_distance = distances[area[0]][area[1]-1]
		if ord(left_height) - ord(height) <= 1 and current_distance + 1 < left_distance:
			distances[area[0]][area[1]-1] = current_distance + 1
			areas_to_check.append([area[0], area[1]-1])

print(distances[goal[0]][goal[1]])


# ********************************
# *            PART 2            *
# ********************************

print("\n*** Part 2 ***")

distances = [[100000 for x in range(len(inputs[0]))] for i in range(len(inputs))]
def get_map_height(y, x):
	if y < 0 or y >= len(inputs) or x < 0 or x >= len(inputs[y]):
		return None
	height = inputs[y][x]
	if height == 'S':
		return 'a'
	elif height == 'E':
		return 'z'
	return height

start = [0,0]
for i in range(len(inputs)):
	if 'E' in inputs[i]:
		start = [i, inputs[i].find('E')]
		distances[start[0]][start[1]] = 0

areas_to_check = [start]
while len(areas_to_check) > 0:
	area = areas_to_check.pop()
	height = get_map_height(area[0], area[1])
	current_distance = distances[area[0]][area[1]]
	
	up_height = get_map_height(area[0]-1, area[1])
	if up_height:
		up_distance = distances[area[0]-1][area[1]]
		if ord(height) - ord(up_height) <= 1 and current_distance + 1 < up_distance:
			distances[area[0]-1][area[1]] = current_distance + 1
			areas_to_check.append([area[0]-1, area[1]])

	right_height = get_map_height(area[0], area[1]+1)
	if right_height:
		right_distance = distances[area[0]][area[1]+1]
		if ord(height) - ord(right_height) <= 1 and current_distance + 1 < right_distance:
			distances[area[0]][area[1]+1] = current_distance + 1
			areas_to_check.append([area[0], area[1]+1])

	down_height = get_map_height(area[0]+1, area[1])
	if down_height:
		down_distance = distances[area[0]+1][area[1]]
		if ord(height) - ord(down_height) <= 1 and current_distance + 1 < down_distance:
			distances[area[0]+1][area[1]] = current_distance + 1
			areas_to_check.append([area[0]+1, area[1]])

	left_height = get_map_height(area[0], area[1]-1)
	if left_height:
		left_distance = distances[area[0]][area[1]-1]
		if ord(height) - ord(left_height) <= 1 and current_distance + 1 < left_distance:
			distances[area[0]][area[1]-1] = current_distance + 1
			areas_to_check.append([area[0], area[1]-1])

closest_a = 100000
for y in range(len(inputs)):
	for x in range(len(inputs[y])):
		if (inputs[y][x] == 'a' or inputs[y][x] == 'S'):
			if distances[y][x] < closest_a:
				closest_a = distances[y][x]

print(closest_a)

end_time = time.time()
time_lapsed = end_time - start_time
print("\nTime elapsed: {0} seconds".format(round(time_lapsed, 5))) 	