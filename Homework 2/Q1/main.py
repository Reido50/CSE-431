import sys

num_tests = int(input())

# Populate nodes
nodes = []
for l in range(num_tests):
    line = input().split()
    nodes.append((int(line[0]), int(line[1])))

# Traverse nodes to find first good starting node
current_start = 0
current_fuel = 0
current_run = 1
for curr in range(len(nodes)):
    current_fuel += nodes[curr][0]
    current_fuel -= nodes[curr][1]
    if current_fuel >= 0:
        current_run += 1
        if curr == len(nodes) - 1:
            print(current_start)
    else:
        current_start = curr + 1
        current_fuel = 0
        current_run = 1
