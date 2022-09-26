num_tests = int(input())

for i in range(num_tests):
    # Get current line of input
    line = input().split()
    x = int(line[0])
    y = int(line[1])
    n = int(line[2])

    # Generate all the combinations
    s = set()
    for p in range(n + 1):
        for q in range(n + 1):
            if p + q == n:
                s.add(p * x + q * y)

    # Print set of combinations sorted
    print(*sorted(s), sep = " ")
