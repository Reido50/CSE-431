import math

# Get input
first_line = input().split()
nodes = int(first_line[0])
edges = int(first_line[1])

# Init graph
graph = {}
for i in range(nodes):
    graph[i] = []

# Populate graph
for i in range(edges):
    connection = input().split()
    first = int(connection[0])
    second = int(connection[1])
    graph[first].append(second)
    graph[second].append(first)

# Find best node
best = -1
most_combs = -1
for i in range(nodes):
    conns = graph[i]
    num_conns = len(conns)
    if num_conns > 1:
        combinations = int(math.factorial(num_conns + 1) / (2 * math.factorial(num_conns + 1 - 2)))

        if best == -1 or combinations > most_combs:
            best = i
            most_combs = combinations

# Print result
print(most_combs)
