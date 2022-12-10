
# Project: 	Advent of Code 2022 - Day 9
# Author: 	Jake Cope
# Date:		12/09/2022

import time

input_file = "input/day9.txt"
inputs = []
with open(input_file, "r") as file:
	inputs = file.read().splitlines() 

start_time = time.time()

# ********************************
# *            PART 1            *
# ********************************

print("\n*** Part 1 ***")

head_location = [0,0]
tail_location = [0,0]
tail_locations = [[0,0]]
for i in range(0, len(inputs)):
	direction = inputs[i][0]
	distance = int(inputs[i][1:])
	for d in range(distance):
		prev_head = head_location.copy()
		if direction == 'R':
			head_location[0] += 1
		elif direction == 'L':
			head_location[0] -= 1
		elif direction == 'U':
			head_location[1] -= 1
		elif direction == 'D':
			head_location[1] += 1
		
		xD = abs(head_location[0] - tail_location[0])
		yD = abs(head_location[1] - tail_location[1])
		if xD >= 2 or yD >= 2:
			tail_location = prev_head.copy()
			if prev_head not in tail_locations:
				tail_locations.append(prev_head)

print(len(tail_locations))


# ********************************
# *            PART 2            *
# ********************************

print("\n*** Part 2 ***")

knot_locations = [[0,0] for i in range(10)]
tail_locations = [[0,0]]
for i in range(0, len(inputs)):
	direction = inputs[i][0]
	distance = int(inputs[i][1:])
	for d in range(distance):
		prev_knots = [knot_locations[c].copy() for c in range(len(knot_locations))]
		if direction == 'R':
			knot_locations[0][0] += 1
		elif direction == 'L':
			knot_locations[0][0] -= 1
		elif direction == 'U':
			knot_locations[0][1] -= 1
		elif direction == 'D':
			knot_locations[0][1] += 1

		diagonal = [0,0]
		for knot in range(1,len(knot_locations)):
			xD = abs(knot_locations[knot-1][0] - knot_locations[knot][0])
			yD = abs(knot_locations[knot-1][1] - knot_locations[knot][1])
			if xD >= 2 or yD >= 2:
				if xD >= 1 and yD >= 1:
					if diagonal == [0,0]:
						diagonal[0] = prev_knots[knot-1][0] - knot_locations[knot][0]
						diagonal[1] = prev_knots[knot-1][1] - knot_locations[knot][1]
					knot_locations[knot][0] += diagonal[0]
					knot_locations[knot][1] += diagonal[1]
				else:
					knot_locations[knot][0] = (knot_locations[knot-1][0] + knot_locations[knot][0]) // 2
					knot_locations[knot][1] = (knot_locations[knot-1][1] + knot_locations[knot][1]) // 2
					diagonal = [0,0]

				if (knot == len(knot_locations)-1):
					tail_location = knot_locations[knot].copy()
					if tail_location not in tail_locations:
						tail_locations.append(tail_location)
			else:
				diagonal = [0,0]

print(len(tail_locations))


end_time = time.time()
time_lapsed = end_time - start_time
print("\nTime elapsed: {0} seconds".format(round(time_lapsed, 5))) 	