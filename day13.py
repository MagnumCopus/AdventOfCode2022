
# Project: 	Advent of Code 2022 - Day 13
# Author: 	Jake Cope
# Date:		12/13/2022

import time
import functools

input_file = "input/day13.txt"
inputs = []
with open(input_file, "r") as file:
	inputs = file.read().splitlines() 

start_time = time.time()

# ********************************
# *            PART 1            *
# ********************************

print("\n*** Part 1 ***")

pair_indices_in_order = []
pair_index = 1
def compare(packet1, packet2):
	index = 0
	while True:
		if index >= len(packet1) and index < len(packet2):
			pair_indices_in_order.append(pair_index)
			return 1
		elif index >= len(packet2) and index < len(packet1):
			return -1
		elif index >= len(packet1) and index >= len(packet2):
			return 2
		elif type(packet1[index]) is int and type(packet2[index]) is int:
			if packet1[index] < packet2[index]:
				pair_indices_in_order.append(pair_index)
				return 1
			elif packet1[index] > packet2[index]:
				return -1
		elif type(packet1[index]) is list and type(packet2[index]) is list:
			compare_ret = compare(packet1[index], packet2[index])
			if compare_ret == 1:
				return 1
			elif compare_ret == -1:
				return -1
		else:
			if type(packet1[index]) is int:
				packet1[index] = [packet1[index]]
			else:
				packet2[index] = [packet2[index]]
			compare_ret = compare(packet1[index], packet2[index])
			if compare_ret == 1:
				return 1
			elif compare_ret == -1:
				return -1
		index += 1

for i in range(0, len(inputs), 3):
	compare(eval(inputs[i]), eval(inputs[i+1]))
	pair_index += 1

print(sum(pair_indices_in_order))


# ********************************
# *            PART 2            *
# ********************************

print("\n*** Part 2 ***")

packets = []
divider_packets = [[[2]], [[6]]]
packets.append(divider_packets[0])
packets.append(divider_packets[1])
for i in range(0, len(inputs), 3):
	packets.append(eval(inputs[i]))
	packets.append(eval(inputs[i+1]))

sorted_packets = []
while len(packets) > 0:
	block = packets.pop(0)
	for i in range(len(packets)):
		if compare(block, packets[i]) < 0:
			break
	else:
		sorted_packets.append(block)
		continue
	packets.append(block)

decoder_key = sorted_packets.index(divider_packets[0]) + 1
decoder_key *= sorted_packets.index(divider_packets[1]) + 1
print(decoder_key)

end_time = time.time()
time_lapsed = end_time - start_time
print("\nTime elapsed: {0} seconds".format(round(time_lapsed, 5))) 	