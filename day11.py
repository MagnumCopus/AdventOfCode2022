
# Project: 	Advent of Code 2022 - Day 11
# Author: 	Jake Cope
# Date:		12/11/2022

import time

input_file = "input/day11.txt"
inputs = []
with open(input_file, "r") as file:
	inputs = file.read().splitlines() 

start_time = time.time()

# ********************************
# *            PART 1            *
# ********************************

print("\n*** Part 1 ***")

monkeys = [{'inspect': 0, 'items': [99, 67, 92, 61, 83, 64, 98], 'operation': lambda item : item * 17, 'test': 3, 'outcome': [2,4]},
		   {'inspect': 0, 'items': [78, 74, 88, 89, 50], 'operation': lambda item : item * 11, 'test': 5, 'outcome': [5,3]},
		   {'inspect': 0, 'items': [98, 91], 'operation': lambda item : item + 4, 'test': 2, 'outcome': [4,6]},
		   {'inspect': 0, 'items': [59, 72, 94, 91, 79, 88, 94, 51], 'operation': lambda item : item * item, 'test': 13, 'outcome': [5,0]},
		   {'inspect': 0, 'items': [95, 72, 78], 'operation': lambda item : item + 7, 'test': 11, 'outcome': [6,7]},
		   {'inspect': 0, 'items': [76], 'operation': lambda item : item + 8, 'test': 17, 'outcome': [2,0]},
		   {'inspect': 0, 'items': [69, 60, 53, 89, 71, 88], 'operation': lambda item : item + 5, 'test': 19, 'outcome': [1,7]},
		   {'inspect': 0, 'items': [72, 54, 63, 80], 'operation': lambda item : item + 3, 'test': 7, 'outcome': [3,1]}]

for turn in range(20):
	for monkey in monkeys:
		for i in range(len(monkey['items'])):
			monkey['inspect'] += 1
			monkey['items'][i] = monkey['operation'](monkey['items'][i])
			monkey['items'][i] //= 3
			test_outcome = monkey['items'][i] % monkey['test'] == 0
			monkeys[monkey['outcome'][test_outcome]]['items'].append(monkey['items'][i])
		monkey['items'] = []

inspects = [monkey['inspect'] for monkey in monkeys]
inspects.sort()
print(inspects[-2] * inspects[-1])

# ********************************
# *            PART 2            *
# ********************************

print("\n*** Part 2 ***")

monkeys = [{'inspect': 0, 'items': [99, 67, 92, 61, 83, 64, 98], 'operation': lambda item : item * 17, 'test': 3, 'outcome': [2,4]},
		   {'inspect': 0, 'items': [78, 74, 88, 89, 50], 'operation': lambda item : item * 11, 'test': 5, 'outcome': [5,3]},
		   {'inspect': 0, 'items': [98, 91], 'operation': lambda item : item + 4, 'test': 2, 'outcome': [4,6]},
		   {'inspect': 0, 'items': [59, 72, 94, 91, 79, 88, 94, 51], 'operation': lambda item : item * item, 'test': 13, 'outcome': [5,0]},
		   {'inspect': 0, 'items': [95, 72, 78], 'operation': lambda item : item + 7, 'test': 11, 'outcome': [6,7]},
		   {'inspect': 0, 'items': [76], 'operation': lambda item : item + 8, 'test': 17, 'outcome': [2,0]},
		   {'inspect': 0, 'items': [69, 60, 53, 89, 71, 88], 'operation': lambda item : item + 5, 'test': 19, 'outcome': [1,7]},
		   {'inspect': 0, 'items': [72, 54, 63, 80], 'operation': lambda item : item + 3, 'test': 7, 'outcome': [3,1]}]

common_test_mod = 1
for m in range(len(monkeys)):
	common_test_mod *= monkeys[m]['test']

for turn in range(10000):
	for monkey in monkeys:
		for i in range(len(monkey['items'])):
			monkey['inspect'] += 1
			monkey['items'][i] = monkey['operation'](monkey['items'][i])
			monkey['items'][i] %= common_test_mod
			test_outcome = monkey['items'][i] % monkey['test'] == 0
			monkeys[monkey['outcome'][test_outcome]]['items'].append(monkey['items'][i])
		monkey['items'] = []

inspects = [monkey['inspect'] for monkey in monkeys]
inspects.sort()
print(inspects[-2] * inspects[-1])


end_time = time.time()
time_lapsed = end_time - start_time
print("\nTime elapsed: {0} seconds".format(round(time_lapsed, 5))) 	