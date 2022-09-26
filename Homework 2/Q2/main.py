num_comms = int(input())

occurs = {}
answer = 0
answer_occurs = 0
for i in range(num_comms):
    comm = int(input())

    if occurs.get(comm) == None:
        occurs[comm] = 1
    else:
        occurs[comm] += 1
    
    if occurs[comm] > answer_occurs:
        answer = comm
        answer_occurs = occurs[answer]

print(answer)
