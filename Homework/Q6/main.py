from audioop import mul
from math import ceil, floor, sqrt

num_tests = int(input())

for l in range(num_tests):
    # Get current line of input
    line = input().split()
    mini = int(line[0])
    maxi = int(line[1])

    # Find all multiples of 12 and perfect squares
    multiples = range(ceil(mini / 12), floor(maxi / 12) + 1)
    squares = range(ceil(sqrt(mini)), floor(sqrt(maxi)) + 1)

    # Init counters
    d = len(multiples)
    s = len(squares)
    b = 0

    # Find where both are true
    for i in squares:
        num = i * i

        if num % 12 == 0:
            b += 1

    # Print result of current line
    print(str(d) + " " + str(s) + " " + str(b))
