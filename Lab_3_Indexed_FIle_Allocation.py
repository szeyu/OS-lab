def delete_file(file, TOTAL_LENGTH):
    print("Delete file from memory:")
    starting_block = int(input("Enter starting block of file: "))
    length = int(input("Enter size of block: "))

    if starting_block < 0 or starting_block + length > TOTAL_LENGTH:
        print("Error: Invalid block range!")
        return

    # Check if file exists
    file_exists = all(file[j] == 1 for j in range(starting_block, starting_block + length))

    if file_exists:
        for j in range(starting_block, starting_block + length):
            file[j] = 0
        print("File successfully deleted from memory.")
    else:
        print("Error: File does not exist in the specified block range!")


def main():
    TOTAL_LENGTH = 60
    file = [0] * TOTAL_LENGTH  # Initialize array with zeros
    allocated_files = []

    while True:
        print("------------------------------------")
        print("1. Allocate file")
        print("2. View memory")
        print("3. Delete a file")
        print("0. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 0:
            print("Program ends")
            break
        elif choice == 1:
            print("Files allocated are:")
            starting_block = int(input("Enter starting block of file: "))
            length = int(input("Enter size of block: "))

            if starting_block < 0 or starting_block + length > TOTAL_LENGTH:
                print("Error: Not enough memory space!")
                continue

            allocation_possible = True

            # Check if blocks are already allocated
            for j in range(starting_block, starting_block + length):
                if file[j] == 1:
                    print("Error: Block already allocated!")
                    allocation_possible = False
                    break

            # Allocate blocks if possible
            if allocation_possible:
                for j in range(starting_block, starting_block + length):
                    file[j] = 1

                allocated_files.append((starting_block, length))
                print("The file is allocated to memory.")

        elif choice == 2:
            print("Blocks | Blocks Status")
            print("-----------------------------")

            # Display memory status in groups of 10
            for i in range(0, TOTAL_LENGTH, 10):
                print(f"{i:2}     | ", end="")
                for j in range(i, min(i + 10, TOTAL_LENGTH)):
                    print(f"{file[j]} ", end="")
                print()

        elif choice == 3:
            '''if not allocated_files:
                print("No allocated files to delete.")
                continue

            print("Enter details of the file to delete:")
            del_start = int(input("Enter starting block of file: "))
            del_length = int(input("Enter size of block: "))

            if (del_start, del_length) in allocated_files:
                # Deallocate memory
                for j in range(del_start, del_start + del_length):
                    file[j] = 0
                allocated_files.remove((del_start, del_length))
                print("The file has been deleted from memory.")
            else:
                print("Error: File not found or invalid starting block or file size.")
            '''
            delete_file(file, TOTAL_LENGTH)

        else:
            print("Choice is not available.")
            print("Program ends.")
            break


if __name__ == "__main__":
    main()