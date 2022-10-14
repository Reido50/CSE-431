
# Get first line of input (Number of total tubes and number of tubes that will explode)
line = input().split()
total_tubes = int(line[0])
exploding_tubes = int(line[1])

# Traverse all the exploding tubes to find the best tube to take
current_best_tube = 0
current_dist = 0
first_iter = True
prev_tube_loc = -1
exploding_tubes = [int(x) for x in input().split()]   # List comprehension implementation taken from https://stackoverflow.com/questions/1574678/efficient-way-to-convert-strings-from-split-function-to-ints-in-python
exploding_tubes.sort()
for tube_loc in exploding_tubes:
    if first_iter:
        current_best_tube = 0
        current_dist = tube_loc
        first_iter = False
    else:
        dist_btw_explodes = tube_loc - prev_tube_loc
        mid_dist = dist_btw_explodes // 2
        if mid_dist > current_dist:
            current_dist = mid_dist
            current_best_tube = prev_tube_loc + mid_dist

    prev_tube_loc = tube_loc

# Compare to last
dist_to_last = (total_tubes - 1) - prev_tube_loc
if dist_to_last > current_dist:
    current_best_tube = total_tubes
    current_dist = dist_to_last
    
print(int(current_dist))
