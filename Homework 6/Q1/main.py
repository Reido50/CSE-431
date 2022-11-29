# Get Input
first_line = input().split()
num_candidates = int(first_line[0])
num_req_skills = int(first_line[1])
req_skills = set(input().split())

candidates = []
for i in range(num_candidates):
    num_skills = int(input())
    skills = set(input().split())
    candidates.append((num_skills, skills))

best = 9999

# req_skills is the set of skills that are requires to be covered by our candidate choices
# num_req_skills is the number of requires skills
# candidates is a list of tuples that represent a candidate (num_skills, skills set)
# num_candidates is the number of available candidates to check

def covers_reqs(s):
    return s.difference(req_skills) == set()

def is_valid(included):
    weight = 0
    for el in included:
        weight += item_weights[el]

    return weight <= weight_limit


def solve_knapsack(included, remaining):
    global best

    if len(included[1]) >= num_req_skills:
        if covers_reqs(included[1]):
            result = included[0]
            if result < best:
                best = result
            return result

    if len(remaining) == 0:
        return 9999

    curr_item = remaining.pop()

    new_included = [included[0] + 1, included[1].union(curr_item[1])]

    incl_value = solve_knapsack(new_included[:], remaining[:])
    excl_value = solve_knapsack(included[:], remaining[:])

    return min(incl_value, excl_value)

remaining = sorted(candidates, key=lambda x: x[0])
print(solve_knapsack([0, set()], remaining))
