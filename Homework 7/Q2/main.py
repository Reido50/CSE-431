import math

# Get input
first_line = input().split()
nodes = int(first_line[0])
edges = int(first_line[1])

# Init graph
graph = {}
pairs = []
for i in range(nodes):
    graph[i] = []

# Populate graph
for i in range(edges):
    connection = input().split()
    first = int(connection[0])
    second = int(connection[1])
    graph[first].append(second)
    graph[second].append(first)
    pairs.append([first, second])

# Find best node
most_combs = -1
for i in range(len(pairs)):
    pair = pairs[i]
    first = pair[0]
    second = pair[1]
    nodes = graph[first] + graph[second]
    node_set = set(nodes)
    num_conns = len(node_set)
    if num_conns > 1:
        combinations = int(math.factorial(num_conns) / (2 * math.factorial(num_conns - 2)))

        if combinations > most_combs:
            most_combs = combinations

# Print result
print(most_combs)
