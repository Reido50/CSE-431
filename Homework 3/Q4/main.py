
# Get first line of input
line = input().split()
num_agents = int(line[0])
current_agent = int(line[1])

# Get second line of input
line = input().split()
dart_colors = {}
for i in range(len(line)):
    dart_colors[line[i]] = i

# Get third line of input
line = input().split()
agent_darts = []
for i in range(len(line)):
    agent_darts.append(dart_colors[line[i]])

# Generate optimal guess
expected_mod = current_agent
for s in dart_colors.keys():
    if ((sum(agent_darts) + dart_colors[s]) % num_agents) == expected_mod:
        print(s)
