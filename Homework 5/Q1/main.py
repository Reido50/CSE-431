# Reid Harry
# Referenced this Geeksforgeeks article for some assistance: https://www.geeksforgeeks.org/maximum-sum-such-that-no-two-elements-are-adjacent/

# -- Get number of bricks --
num_bricks = int(input())

# -- Get bricks --
bricks = [int(x) for x in input().split()]   # List comprehension implementation taken from https://stackoverflow.com/questions/1574678/efficient-way-to-convert-strings-from-split-function-to-ints-in-python

# -- Calculate Total --
if len == 1:
    print(bricks[0])
else:
    # Make helper array
    helper_arr = []
    for i in range(num_bricks):
        helper_arr.append([0, 0])

    # Init starting values
    helper_arr[0][0] = 0
    helper_arr[0][1] = bricks[0]

    # Traverse bricks to find the two possible solutions
    for i in range(1, num_bricks):
        helper_arr[i][1] = helper_arr[i-1][0] + bricks[i]
        helper_arr[i][0] = max(helper_arr[i-1][1], helper_arr[i - 1][0])

    # Determine which of the solutions is bigger
    total = max(helper_arr[num_bricks - 1][0], helper_arr[num_bricks - 1][1])

# -- Print results --
print(total)
