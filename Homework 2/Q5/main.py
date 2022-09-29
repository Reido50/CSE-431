from queue import PriorityQueue
from tracemalloc import start

num_jobs = int(input())

jobs = PriorityQueue()

# Populate jobs
for i in range(num_jobs):
    line = input().split()
    start_time = int(line[0])
    duration = int(line[1])

    jobs.put((start_time, duration))

# Go through jobs
current_job = jobs.get()
next_job = jobs.get()
current_job_start = current_job[0]
current_job_time = current_job[1]
next_job_start = next_job[0]
next_job_time = next_job[1]
time = current_job[0]

job_queue = PriorityQueue()
jobs_done = 0
total_job_time = 0
while jobs_done < num_jobs:
    # Get all other jobs at this time
    while (time == next_job_start):
        job_queue.put(next_job_time)
        next_job = jobs.get()
        next_job_start = next_job[0]
        next_job_time = next_job[1]

    while (time < next_job_start):
        # Finish current job
        jobs_done += 1
        time += current_job_time
        total_job_time += current_job_time

        # Grab new job
        current_job_time = job_queue.get()

print(total_job_time // num_jobs)
