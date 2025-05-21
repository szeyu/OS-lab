def first_fit_memory_allocation(blocks, files):
    n_blocks = len(blocks)
    n_files = len(files)
    allocation = [-1] * n_files
    fragment = [None] * n_files
    block_sizes = blocks[:]

    for i in range(n_files):
        for j in range(n_blocks):
            if block_sizes[j] >= files[i]:
                allocation[i] = j
                fragment[i] = block_sizes[j] - files[i]
                block_sizes[j] = -1  # Mark block as used
                break

    print("\nFile No\tFile Size\tBlock No\tBlock Size\tFragment")
    for i in range(n_files):
        if allocation[i] != -1:
            print(f"{i + 1}\t\t{files[i]}\t\t\t{allocation[i] + 1}\t\t\t{blocks[allocation[i]]}\t\t\t{fragment[i]}")
        else:
            print(f"{i + 1}\t\t{files[i]}\t\t\t-\t\t\t-\t\t\tNot Allocated")



# Input Section
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

# Run First-Fit Allocation
first_fit_memory_allocation(blocks, files)
