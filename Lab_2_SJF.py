class Job:
    def __init__(self, process_id):
        self.process_id = process_id
        self.arrival_time = 0
        self.burst_time = 0
        self.completion_time = 0
        self.waiting_time = 0
        self.turnaround_time = 0
        self.isComplete = False

    # less than 
    def __lt__(self, other):
        return self.burst_time < other.burst_time

num_of_process = int(input("Enter the number of process: "))

# Initialize list of jobs on user input
jobs = [Job(i + 1) for i in range(num_of_process)]

for job in jobs:
    job.arrival_time = int(input(f'Enter arrival time for P{job.process_id}: '))
    job.burst_time = int(input(f'Enter burst time for P{job.process_id}: '))
    print()

current_time = 0
completed_process = 0
total_waiting_time = 0
total_turnaround_time = 0
job_order = []

while completed_process < num_of_process:
    waiting_queue = []

    for job in jobs:
        # Check if job has arrived and is not complete
        if job.arrival_time <= current_time and not job.isComplete:
            waiting_queue.append(job)

    if waiting_queue:
        waiting_queue.sort()
        current_job = waiting_queue[0]

        current_time = max(current_time, current_job.arrival_time)
        current_job.completion_time = current_time + current_job.burst_time
        current_job.turnaround_time = current_job.completion_time - current_job.arrival_time
        current_job.waiting_time = current_job.turnaround_time - current_job.burst_time
        current_job.isComplete = True

        total_waiting_time += current_job.waiting_time
        total_turnaround_time += current_job.turnaround_time
        current_time = current_job.completion_time
        job_order.append(current_job)
        completed_process += 1
    else:
        current_time += 1 

print('\nProcess ID | Arrival Time | Burst Time | Waiting Time | Turnaround Time |')
for job in job_order:
    print(f'{job.process_id:10} | {job.arrival_time:12} | {job.burst_time:10} | {job.waiting_time:12} | {job.turnaround_time:15} |')

print(f'\nAverage waiting time: {total_waiting_time / num_of_process:.2f}')
print(f'Average turnaround time: {total_turnaround_time / num_of_process:.2f}')

