# Get input
num_tests = int(input())
contestants = input().split()

# Init counter variables
prev_count = len(contestants)
curr_count = prev_count
time = 0

print(prev_count)   # Initial count print

while curr_count > 0:
    # If the count has changed, print the current count
    if curr_count != prev_count:
        print(curr_count)
        prev_count = curr_count

    time += 1

    # Find all contestants that are eliminated at the new time
    for a in contestants:
        if int(a) == time:
            curr_count -= 1

