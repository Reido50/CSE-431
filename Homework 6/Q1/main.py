import random

best = 0

def binpack(items, capacity, current_solution):

    global best

    if sum(current_solution) > capacity:
        return 0

    if sum(current_solution) + sum(items) <= best:
        return 0

    if len(items) == 0:
        result = sum(current_solution)
        if result > best:
            best = result
        return sum(current_solution)

    curr_item = items.pop()
    included = binpack(items[:], capacity, current_solution + [curr_item])
    excluded = binpack(items[:], capacity, current_solution)

    return max(included, excluded)


first = input().split()
candidates = int(first[0])
skill_count = int(first[1])
skill_list = input().split()

print(binpack(skill_list, candidates, []))