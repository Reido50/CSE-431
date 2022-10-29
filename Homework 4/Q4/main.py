num_tests = int(input())

for i in range(num_tests):
    line = input().split()
    lock_start = int(line[0])
    lock_goal = int(line[1])

    lock_difference = lock_start - lock_goal

    ops = 0
    for i in range(64):
        if (lock_difference & (1 << i)):
            ops += 1

    print(ops)
