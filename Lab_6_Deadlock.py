P = 4  # Number of processes
R = 3  # Number of resources


def display_processes(allocated, max_demand):
    print("Process\t\tAllocation\t\t\tMax\t\t\t\tNeed")
    print("\t\t\tA\tB\tC\t\tA\tB\tC\t\tA\tB\tC")

    for i in range(P):
        print(f"P{i}\t\t\t", end="")
        for j in range(R):
            print(f"{allocated[i][j]}\t", end="")
        print("\t", end="")
        for j in range(R):
            print(f"{max_demand[i][j]}\t", end="")
        print("\t", end="")

        need = [max_demand[i][j] - allocated[i][j] for j in range(R)]
        for j in range(R):
            if need[j] < 0:
                print("\nWarning: Current Condition is not safe.")
                exit(-1)
            print(f"{need[j]}\t", end="")
        print()


def bankers_algorithm(max_demand, allocated, max_capacity):
    print("Maximum Resources in the System:", " ".join(map(str, max_capacity)))

    need = []
    for i in range(P):
        row = []
        for j in range(R):
            value = max_demand[i][j] - allocated[i][j]
            row.append(value)
        need.append(row)

    available = []
    for j in range(R):
        total_allocated = 0
        for i in range(P):
            total_allocated += allocated[i][j]
        remaining = max_capacity[j] - total_allocated
        available.append(remaining)

    print("***********************************************************************************")
    display_processes(allocated, max_demand)
    print("\nRemaining available resources:", " ".join(map(str, available)))

    completed = [0] * P
    safe_sequence = []
    count = 0

    while count < P:
        found = False
        for i in range(P):
            if completed[i] == 0:
                if all(need[i][j] <= available[j] for j in range(R)):
                    print("Current condition is safe")
                    print("***********************************************************************************")
                    completed[i] = 1
                    safe_sequence.append(i)
                    count += 1
                    for j in range(R):
                        available[j] += allocated[i][j]
                        allocated[i][j] = 0
                        need[i][j] = 0
                    print(f"Remaining available resources are now allocated to P{i} to finish the process.")
                    print(f"P{i} is done. Releasing resources back to remaining available.")
                    print("**********************************************************************************")
                    display_processes(allocated, max_demand)
                    print("\nRemaining available resources:", " ".join(map(str, available)))
                    found = True
                    break
        if not found:
            break

    if count == P:
        print("The system is at a safe state.")
        print("Safe sequence:", " ".join(f"P{p}" for p in safe_sequence))
    else:
        print("The system is in an unsafe state.")


if __name__ == "__main__":
    max_demand = [
        [2, 2, 2],
        [3, 2, 2],
        [9, 0, 2],
        [4, 3, 3]
    ]
    allocated = [
        [2, 1, 1],
        [2, 0, 0],
        [3, 0, 2],
        [0, 0, 2]
    ]
    max_capacity = [10, 5, 7]

    print(f"Number of Processes: {P}")
    print(f"Number of Resources: {R}")
    bankers_algorithm(max_demand, allocated, max_capacity)
