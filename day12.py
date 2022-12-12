
# Project: 	Advent of Code 2022 - Day 12
# Author: 	Jake Cope
# Date:		12/12/2022

import time
import sys

sys.setrecursionlimit(1500)

input_file = "input/day12.txt"
inputs = []
with open(input_file, "r") as file:
	inputs = file.read().splitlines() 

start_time = time.time()

# ********************************
# *            PART 1            *
# ********************************

print("\n*** Part 1 ***")

best_scores = [[100000 for x in range(len(inputs[0]))] for i in range(len(inputs))]
lowest_from_a = 100000
def get_map_height(y, x):
	if y < 0 or y >= len(inputs) or x < 0 or x >= len(inputs[y]):
		return None
	height = inputs[y][x]
	if height == 'S':
		return 'a'
	elif height == 'E':
		return 'z'
	return height

def move(y, x, visited):
	global lowest_from_a
	global best_scores
	new_visited = []
	for visit in visited:
		new_visited.append(visit.copy())
	new_visited.append([y,x])
	best_scores[y][x] = len(new_visited)

	if inputs[y][x] == 'E':
		new_visited.reverse()
		for i in range(len(new_visited)):
			if get_map_height(new_visited[i][0], new_visited[i][1]) == 'a':
				if i < lowest_from_a:
					lowest_from_a = i
		return 0;

	current = get_map_height(y, x)
	distance_from_goal = 100000

	up = [y-1,x]
	up_step = get_map_height(up[0], up[1])
	if up_step and up not in new_visited and ord(up_step)-ord(current) <= 1 and best_scores[up[0]][up[1]] > len(new_visited) + 1:
		up_distance = move(up[0], up[1], new_visited)
		if up_distance < distance_from_goal:
			distance_from_goal = up_distance

	right = [y,x+1]
	right_step = get_map_height(right[0], right[1])
	if right_step and right not in new_visited and ord(right_step)-ord(current) <= 1 and best_scores[right[0]][right[1]] > len(new_visited) + 1:
		right_distance = move(right[0], right[1], new_visited)
		if right_distance < distance_from_goal:
			distance_from_goal = right_distance
	
	down = [y+1,x]
	down_step = get_map_height(down[0], down[1])
	if down_step and down not in new_visited and ord(down_step)-ord(current) <= 1 and best_scores[down[0]][down[1]] > len(new_visited) + 1:
		down_distance = move(down[0], down[1], new_visited)
		if down_distance < distance_from_goal:
			distance_from_goal = down_distance

	left = [y,x-1]
	left_step = get_map_height(left[0], left[1])
	if left_step and left not in new_visited and ord(left_step)-ord(current) <= 1 and best_scores[left[0]][left[1]] > len(new_visited) + 1:
		left_distance = move(left[0], left[1], new_visited)
		if left_distance < distance_from_goal:
			distance_from_goal = left_distance

	return distance_from_goal + 1

starting_position = [0,0]
for i in range(len(inputs)):
	if 'S' in inputs[i]:
		starting_position = [i, inputs[i].find('S')]
print(move(starting_position[0], starting_position[1], []))


# ********************************
# *            PART 2            *
# ********************************

print("\n*** Part 2 ***")

print(lowest_from_a)


end_time = time.time()
time_lapsed = end_time - start_time
print("\nTime elapsed: {0} seconds".format(round(time_lapsed, 5))) 	