import random
import math

# Get input
first_line = input().split()
nodes = int(first_line[0])
edges = int(first_line[1])

# Init graph
graph = {}
untraversed = {}
islands = 0
for i in range(nodes):
    graph[i] = []
    untraversed[i] = 1

# Populate graph
for i in range(edges):
    connection = input().split()
    first = int(connection[0])
    second = int(connection[1])
    graph[first].append(second)
    graph[second].append(first)

def dfs(start_node):
    # Init
    stack = [start_node]
    discovered = {}
    discovered[start_node] = 1

    while len(stack) != 0:
        # Grab current node and neighboors
        cur = stack.pop()
        neighboors = graph[cur]

        # Traverse current
        untraversed.pop(cur)

        # Add undiscovered neighboors to stack
        for n in neighboors:
            if discovered.get(n) == None:
                discovered[n] = 1
                stack.append(n)

while len(untraversed) != 0:
    # Pick a random untraversed node
    # Source: https://stackoverflow.com/questions/4859292/how-to-get-a-random-value-from-dictionary
    rand_node = random.choice(list(untraversed.keys()))

    # Do DFS on random node
    dfs(rand_node)

    # Increment counter
    islands += 1

print(islands)
