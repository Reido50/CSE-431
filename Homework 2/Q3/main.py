from heapq import heappop, heappush, heapify

num_commands = int(input())

# Deal with commands
heap = []
heapify(heap)
stack = []
for i in range(num_commands):
    command = input().split()

    if int(command[0]) == 1:
        # Add an Email
        heappush(heap, (int(command[1]) * -1))
        heapify(heap)
        stack.append(int(command[1]))
    elif int(command[0]) == 2:
        # Pop an Email
        popped = stack.pop()
        heap.remove(popped * -1)
        heapify(heap)
    elif int(command[0]) == 3:
        # Print most important email
        print(heap[0] * -1)
