
# Project: 	Advent of Code 2022 - Day 8
# Author: 	Jake Cope
# Date:		12/08/2022

import time

input_file = "input/day8.txt"
inputs = []
with open(input_file, "r") as file:
	inputs = file.read().splitlines() 

start_time = time.time()

# ********************************
# *            PART 1            *
# ********************************

print("\n*** Part 1 ***")

trees = 0
for y in range(0, len(inputs)):
	for x in range(0, len(inputs[y])):
		tree_height = inputs[y][x]
		up_shorter = True
		down_shorter = True
		left_shorter = True
		right_shorter = True
		for yD in range(y-1, -1, -1):
			if inputs[yD][x] >= tree_height:
				up_shorter = False
				break;
		for yD in range(y+1, len(inputs), 1):
			if inputs[yD][x] >= tree_height:
				down_shorter = False
				break;
		for xD in range(x-1, -1, -1):
			if inputs[y][xD] >= tree_height:
				left_shorter = False
				break;
		for xD in range(x+1, len(inputs[y]), 1):
			if inputs[y][xD] >= tree_height:
				right_shorter = False
				break;
		if up_shorter or down_shorter or left_shorter or right_shorter:
			trees += 1
print(trees)


# ********************************
# *            PART 2            *
# ********************************

print("\n*** Part 2 ***")

best_score = 0
for y in range(0, len(inputs)):
	for x in range(0, len(inputs[y])):
		tree_height = inputs[y][x]
		up_score = 0
		down_score = 0
		left_score = 0
		right_score = 0
		for yD in range(y-1, -1, -1):
			up_score += 1
			if inputs[yD][x] >= tree_height:
				break;
		for yD in range(y+1, len(inputs), 1):
			down_score += 1
			if inputs[yD][x] >= tree_height:
				break;
		for xD in range(x-1, -1, -1):
			left_score += 1
			if inputs[y][xD] >= tree_height:
				break;
		for xD in range(x+1, len(inputs[y]), 1):
			right_score += 1
			if inputs[y][xD] >= tree_height:
				break;
		score = up_score * down_score * left_score * right_score
		if score > best_score:
			best_score = score
print(best_score)


end_time = time.time()
time_lapsed = end_time - start_time
print("\nTime elapsed: {0} seconds".format(round(time_lapsed, 5)))