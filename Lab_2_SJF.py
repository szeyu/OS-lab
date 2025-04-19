class Job:
    def __init__(self, process_id):
        self.process_id = process_id
        self.burst_time = 0
        self.completion_time = 0
        self.waiting_time = 0
        self.turnaround_time = 0

    # less than 
    def __lt__(self, other):
        return self.burst_time < other.burst_time
    

num_of_process = int(input("Enter the number of process: "))

# Initialize list of jobs on user input
jobs = [Job(i + 1) for i in range(num_of_process)]

for job in jobs:
    job.burst_time = int(input(f'Enter burst time for P{job.process_id}: '))

jobs.sort() # Calls the __lt__ method

total_waiting_time = 0
total_turnaround_time = 0

for i, job in enumerate(jobs):
    if(i == 0):
        job.completion_time = job.burst_time
        job.turnaround_time = job.completion_time
    else:
        prev = i - 1
        job.completion_time = jobs[prev].completion_time + job.burst_time
        job.waiting_time = jobs[prev].completion_time 
        job.turnaround_time = job.completion_time # Assume all arrive at 0
    
    total_waiting_time += job.waiting_time
    total_turnaround_time += job.turnaround_time



print('Process ID | Burst Time | Waiting Time | Turnaround Time | ')
for job in jobs:
    print(f'{job.process_id:10} | {job.burst_time:10} | {job.waiting_time:12} | {job.turnaround_time:15} |')

print(f'Average waiting time: {total_waiting_time / num_of_process:.2f}')
print(f'Average turnaround time: {total_turnaround_time / num_of_process:.2f}')

