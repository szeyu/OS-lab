def fcfs_scheduling(processes, burst_times):
    n = len(processes)
    waiting_time = [0] * n
    turnaround_time = [0] * n
    start_time = [0] * n
    completion_time = [0] * n

    # First process starts at time 0
    start_time[0] = 0
    completion_time[0] = burst_times[0]
    turnaround_time[0] = burst_times[0]
    waiting_time[0] = 0

    # Loop through remaining processes
    for i in range(1, n):
        start_time[i] = completion_time[i - 1]
        completion_time[i] = start_time[i] + burst_times[i]
        turnaround_time[i] = completion_time[i]
        waiting_time[i] = turnaround_time[i] - burst_times[i]

    # Output results
    print("\nProcess | Burst Time | Waiting Time | Turnaround Time")
    for i in range(n):
        print(f"  P{processes[i]}     |     {burst_times[i]}      |      {waiting_time[i]}       |        {turnaround_time[i]}")

    # Averages
    avg_wt = sum(waiting_time) / n
    avg_tat = sum(turnaround_time) / n
    print(f"\nAverage Waiting Time: {avg_wt:.2f}")
    print(f"Average Turnaround Time: {avg_tat:.2f}")

def main():
    print("FCFS CPU Scheduling Simulation")
    n = int(input("Enter the number of processes: "))

    processes = []
    burst_times = []

    for i in range(n):
        processes.append(i + 1)
        bt = int(input(f"Enter burst time for Process P{i + 1}: "))
        burst_times.append(bt)

    fcfs_scheduling(processes, burst_times)

# Run the program
if __name__ == "__main__":
    main()
