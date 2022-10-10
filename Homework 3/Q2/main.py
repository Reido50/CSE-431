# Get first line of input
line = input().split()
num_plans = int(line[0])
num_agents = int(line[1])

# Traverse the plans
plans = [int(x) for x in input().split()]   # List comprehension implementation taken from https://stackoverflow.com/questions/1574678/efficient-way-to-convert-strings-from-split-function-to-ints-in-python
plans.sort(reverse=True)
cost = 0
for i in range(0, num_plans, num_agents):
    for j in range(num_agents):
        if i + j < num_plans:
            cost += (plans[i + j] * ((i // num_agents) + 1))

# Print total cost
print(cost)
