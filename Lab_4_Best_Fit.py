# Best-Fit Memory Allocation with Fragment and Table Output

def best_fit_memory_allocation(blocks, files):
    n_blocks = len(blocks)
    n_files = len(files)
    allocation = [-1] * n_files
    fragment = [None] * n_files
    block_sizes = blocks[:]

    for i in range(n_files):
        best_index = -1
        for j in range(n_blocks):
            if block_sizes[j] >= files[i]:
                if best_index == -1 or block_sizes[j] < block_sizes[best_index]:
                    best_index = j

        if best_index != -1:
            allocation[i] = best_index
            fragment[i] = block_sizes[best_index] - files[i]
            block_sizes[best_index] = -1  # Mark block as used

    print("\nFile No\tFile Size\tBlock No\tBlock Size\tFragment")
    for i in range(n_files):
        print(f"{i + 1}\t{files[i]}\t\t", end="")
        if allocation[i] != -1:
            block_no = allocation[i] + 1
            block_size = blocks[allocation[i]]
            print(f"{block_no}\t\t{block_size}\t\t{fragment[i]}")
        else:
            print("-\t\t-\t\tNot Allocated")

# Input section
blocks = []
files = []

n_blocks = int(input("Enter the number of blocks: "))
n_files = int(input("Enter the number of files: "))

print("\nEnter the size of the blocks:")
for i in range(n_blocks):
    size = int(input(f"Block {i+1}: "))
    blocks.append(size)

print("\nEnter the size of the files:")
for i in range(n_files):
    size = int(input(f"File {i+1}: "))
    files.append(size)

# Run Best-Fit Allocation
best_fit_memory_allocation(blocks, files)
