import email
from heapq import heappop, heappush, heapify

num_commands = int(input())

# Deal with commands
stack = []
max_stack = []
for i in range(num_commands):
    line = input().split()
    command = int(line[0])

    if command == 1:
        # Add an Email
        email_prio = int(line[1])
        stack.append(email_prio)
        if len(stack) == 1 or email_prio > max_stack[-1]:
            max_stack.append(email_prio)
        else:
            max_stack.append(max_stack[-1])
    elif command == 2:
        # Pop an Email
        stack.pop()
        max_stack.pop()
    elif command == 3:
        # Print most important email
        print(max_stack[-1])
