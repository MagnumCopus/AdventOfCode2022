
# Project: 	Advent of Code 2022 - Day 14
# Author: 	Jake Cope
# Date:		12/14/2022

import time
import functools

input_file = "input/day14.txt"
inputs = []
with open(input_file, "r") as file:
	inputs = file.read().splitlines() 

start_time = time.time()

# ********************************
# *            PART 1            *
# ********************************

print("\n*** Part 1 ***")

biggest_x = 0
biggest_y = 0
for i in range(len(inputs)):
	coords = inputs[i].split(' -> ')
	for c in coords:
		(x, y) = c.split(',')
		if int(x) > biggest_x:
			biggest_x = int(x)
		if int(y) > biggest_y:
			biggest_y = int(y)

cave = [[' ' for x in range(biggest_x+100)] for y in range(biggest_y+1)]

for i in range(len(inputs)):
	coords = inputs[i].split(' -> ')
	last_coord = []
	for c in range(len(coords)):
		(x, y) = coords[c].split(',')
		x = int(x)
		y = int(y)
		if last_coord == []:
			cave[y][x] = '#'
		else:
			new_x = x
			new_y = y
			while last_coord[0] != new_y or last_coord[1] != new_x:
				cave[new_y][new_x] = '#'
				if new_y < last_coord[0]:
					new_y += 1
				elif new_y > last_coord[0]:
					new_y -= 1
				elif new_x < last_coord[1]:
					new_x += 1
				elif new_x > last_coord[1]:
					new_x -= 1
		last_coord = [y, x]

sand = 0
while True:
	sand_y = 0
	sand_x = 500
	void = False
	while True:
		if sand_y == len(cave)-1:
			void = True
			break
		if cave[sand_y+1][sand_x] == ' ':
			sand_y += 1
		elif cave[sand_y+1][sand_x-1] == ' ':
			sand_y += 1
			sand_x -= 1
		elif cave[sand_y+1][sand_x+1] == ' ':
			sand_y += 1
			sand_x += 1
		else:
			cave[sand_y][sand_x] = 'o'
			break
	if void:
		break
	sand += 1
print(sand)



# ********************************
# *            PART 2            *
# ********************************

print("\n*** Part 2 ***")


biggest_x = 0
biggest_y = 0
for i in range(len(inputs)):
	coords = inputs[i].split(' -> ')
	for c in coords:
		(x, y) = c.split(',')
		if int(x) > biggest_x:
			biggest_x = int(x)
		if int(y) > biggest_y:
			biggest_y = int(y)

cave = [[' ' for x in range(biggest_x+200)] for y in range(biggest_y+2)]
cave.append(['#' for x in range(biggest_x+200)])

for i in range(len(inputs)):
	coords = inputs[i].split(' -> ')
	last_coord = []
	for c in range(len(coords)):
		(x, y) = coords[c].split(',')
		x = int(x)
		y = int(y)
		if last_coord == []:
			cave[y][x] = '#'
		else:
			new_x = x
			new_y = y
			while last_coord[0] != new_y or last_coord[1] != new_x:
				cave[new_y][new_x] = '#'
				if new_y < last_coord[0]:
					new_y += 1
				elif new_y > last_coord[0]:
					new_y -= 1
				elif new_x < last_coord[1]:
					new_x += 1
				elif new_x > last_coord[1]:
					new_x -= 1
		last_coord = [y, x]

sand = 0
while True:
	sand_y = 0
	sand_x = 500
	done = False
	sand += 1
	while True:
		if cave[sand_y+1][sand_x] == ' ':
			sand_y += 1
		elif cave[sand_y+1][sand_x-1] == ' ':
			sand_y += 1
			sand_x -= 1
		elif cave[sand_y+1][sand_x+1] == ' ':
			sand_y += 1
			sand_x += 1
		else:
			if sand_y == 0 and sand_x == 500:
				print(sand)
				done = True
			cave[sand_y][sand_x] = 'o'
			break
	if done:
		break



end_time = time.time()
time_lapsed = end_time - start_time
print("\nTime elapsed: {0} seconds".format(round(time_lapsed, 5))) 	