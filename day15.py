
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

def dist(p1, p2):
	return abs(p2[1]-p1[1]) + abs(p2[0]-p1[0])

y_to_look = 2000000
beacons = []
not_possible = []
for i in range(len(inputs)):
	command = inputs[i].split(' ')
	sensor_x = int(command[2][2:-1])
	sensor_y = int(command[3][2:-1])
	beacon_x = int(command[8][2:-1])
	beacon_y = int(command[9][2:])
	if [beacon_y, beacon_x] not in beacons:
		beacons.append([beacon_y, beacon_x])
	x_to_beacon = abs(sensor_x - beacon_x)
	dist_to_beacon = dist([sensor_y, sensor_x], [beacon_y, beacon_x])
	min_x_to_check = sensor_x-dist_to_beacon
	max_x_to_check = sensor_x+dist_to_beacon
	left_x = None
	right_x = None
	for x in range(min_x_to_check, max_x_to_check):
		checking = [y_to_look, x]
		if dist([sensor_y, sensor_x], checking) <= dist_to_beacon:
			not_possible.append([x, (sensor_x - x) + sensor_x])
			break

min_x = 10000000000000000000000
max_x = 0
for n in not_possible:
	if n[0] < min_x:
		min_x = n[0]
	elif n[0] > max_x:
		max_x = n[0]
	if n[1] < min_x:
		min_x = n[1]
	elif n[1] > max_x:
		max_x = n[1]

p = max_x-min_x+1

for beacon in beacons:
	if beacon[0] == y_to_look and beacon[1] >= min_x and beacon[1] <= max_x:
		p -= 1

print(p)


# ********************************
# *            PART 2            *
# ********************************

print("\n*** Part 2 ***")

def dist(p1, p2):
	return abs(p2[1]-p1[1]) + abs(p2[0]-p1[0])

bound = 4000000
sensors = []
def in_bounds(p):
	if p[0] < 0 or p[0] > bound or p[1] < 0 or p[1] > bound:
		return False

	for sensor in sensors:
		if dist(p,sensor[0]) <= sensor[1]:
			return False

	return True

circumference = []
for i in range(len(inputs)):
	print(len(circumference))
	command = inputs[i].split(' ')
	sensor_x = int(command[2][2:-1])
	sensor_y = int(command[3][2:-1])
	beacon_x = int(command[8][2:-1])
	beacon_y = int(command[9][2:])
	dist_to_beacon = dist([sensor_y, sensor_x], [beacon_y, beacon_x])
	sensors.append([[sensor_y, sensor_x], dist_to_beacon])
	x_scan = sensor_x - dist_to_beacon - 1
	y_scan = sensor_y
	while True:
		if x_scan == sensor_x:
			break
		if in_bounds([y_scan, x_scan]):
			circumference.append([y_scan, x_scan])
		if in_bounds([y_scan, (sensor_x-x_scan)+sensor_x]):
			circumference.append([y_scan, (sensor_x-x_scan)+sensor_x])
		if in_bounds([(sensor_y-y_scan)+sensor_y, x_scan]):
			circumference.append([(sensor_y-y_scan)+sensor_y, x_scan])
		if in_bounds([(sensor_y-y_scan)+sensor_y, (sensor_x-x_scan)+sensor_x]):
			circumference.append([(sensor_y-y_scan)+sensor_y, (sensor_x-x_scan)+sensor_x])
		y_scan -= 1
		if in_bounds([y_scan, x_scan]):
			circumference.append([y_scan, x_scan])
		if in_bounds([y_scan, (sensor_x-x_scan)+sensor_x]):
			circumference.append([y_scan, (sensor_x-x_scan)+sensor_x])
		if in_bounds([(sensor_y-y_scan)+sensor_y, x_scan]):
			circumference.append([(sensor_y-y_scan)+sensor_y, x_scan])
		if in_bounds([(sensor_y-y_scan)+sensor_y, (sensor_x-x_scan)+sensor_x]):
			circumference.append([(sensor_y-y_scan)+sensor_y, (sensor_x-x_scan)+sensor_x])
		x_scan += 1

for sensor in sensors:
	print(len(circumference))
	new_cum = []
	for i in range(len(circumference)-1, -1, -1):
		if dist(circumference[i],sensor[0]) > sensor[1]:
			new_cum.append(circumference[i])
	circumference = new_cum

print(circumference)


end_time = time.time()
time_lapsed = end_time - start_time
print("\nTime elapsed: {0} seconds".format(round(time_lapsed, 5))) 	