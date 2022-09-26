from audioop import mul

def standardizeBet(S):
    while S > 1000000:
        S = S - 1000000
    while S < 0:
        S = S + 1000000
    return S
    

num_tests = int(input())
results = []

for test_idx in range(num_tests):
    line = input().split()
    S = int(line[0]) # Starting bet
    k = int(line[1]) # Number of rounds

    for i in range(k):
        # Assume bet is even
        subtract = 99
        mult = 3

        # Determine if bet is odd
        # Had to look up bitwise ops in Python at https://realpython.com/python-bitwise-operators/
        if S & 1:
            # Bet is odd
            subtract = 15
            mult = 2

        # Do subtraction
        S = S - subtract
        S = standardizeBet(S)

        # Do multiplication
        S = S * mult
        S = standardizeBet(S)

    # End of current test
    results.append(S)

# End of all tests
print(*results , sep = "\n")
        