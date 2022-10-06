# Get first line of input
first_line = input().split()
num_plans = int(first_line[0])
num_foils = int(first_line[1])

# Get plans input
plans = []
for i in range(num_plans):
    plans.append(int(input()))

# Sort plans
plans.sort()

# Print the highest plans you can foil
for i in range(len(plans) - 1, len(plans) - 1 - num_foils, -1):
    print(plans[i])
