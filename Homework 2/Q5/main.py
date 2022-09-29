from queue import PriorityQueue

num_jobs = int(input())

jobs = PriorityQueue()

# Populate jobs
for i in range(num_jobs):
    line = input().split()
    start_time = int(line[0])
    duration = int(line[1])

    jobs.put((start_time, duration))

# Grab first job and peek next_job
peek_job = jobs.get()
peek_job_start = peek_job[0]
peek_job_dur = peek_job[1]

current_job = None
current_job_dur = 0
current_job_start = 0

time = peek_job_start

job_dur_queue = PriorityQueue()
jobs_done = 0
total_job_time = 0
while jobs_done < num_jobs:
    # Get all jobs at this time
    while (peek_job_start <= time and peek_job is not None):
        job_dur_queue.put((peek_job_dur, peek_job_start))
        if (not jobs.empty()):
            peek_job = jobs.get()
            peek_job_start = peek_job[0]
            peek_job_dur = peek_job[1]
        else:
            peek_job = None

    # Grab current job
    if (not job_dur_queue.empty()):
        current_job = job_dur_queue.get()
        current_job_dur = current_job[0]
        current_job_start = current_job[1]
    else:
        current_job = None

    # Do current job
    if (current_job is not None):
        jobs_done += 1
        time += current_job_dur
        total_job_time += (time - current_job_start)
        current_job = None
    else:
        time = peek_job_start

print(total_job_time // num_jobs)
