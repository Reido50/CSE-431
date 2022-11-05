# -- Get number of bricks --
num_bricks = int(input())

# -- Get bricks --
bricks = [int(x) for x in input().split()]   # List comprehension implementation taken from https://stackoverflow.com/questions/1574678/efficient-way-to-convert-strings-from-split-function-to-ints-in-python

# -- Make list of net speed values --
net_speeds = []
for i in range(num_bricks):
    net = 0

    # -- Add current value as positive --
    net += bricks[i]

    # -- Add neighbor values as negative --
    # Left neighbor
    if i > 0:
        net -= bricks[i - 1]
    # Right neighbor
    if i < (num_bricks - 1):
        net -= bricks[i + 1]

    net_speeds.append(net)

# -- Find the elements with the highest net_speeds
total = 0
start = 0
end = num_bricks - 1
while(True):
    # -- Find the highest of the first ~3 --
    sub_arr_end = min(start + 2, end)
    sub_arr_one = bricks[start : sub_arr_end + 1] # THIS LINE IS HERE FOR DEBUGGING PURPOSES
    highest = start
    for j in range(start + 1, sub_arr_end + 1):
        if net_speeds[j] > net_speeds[highest]:
            highest = j

    # -- Add to total --
    total += bricks[highest]

    # -- Increment start --
    start = highest + 2

    # -- Check if we're done --
    if start > end:
        break

    # -- Find the highest of the last ~3 --
    sub_arr_start = max(end - 2, start)
    sub_arr_two = bricks[sub_arr_start : end + 1] # THIS LINE IS HERE FOR DEBUGGING PURPOSES
    highest = end
    for j in range(end - 1, sub_arr_start - 1, -1):
        if net_speeds[j] > net_speeds[highest]:
            highest = j

    # -- Add to total --
    total += bricks[highest]

    # -- Decrement end --
    end = highest - 2

    # -- Check if we're done --
    if start > end:
        break

# -- Print results --
print(total)
