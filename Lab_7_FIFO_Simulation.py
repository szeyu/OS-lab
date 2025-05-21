def fifo_page_replacement():
    # Get user input for number of frames
    num_frames = int(input("Enter the number of frames: "))
    
    # Get user input for reference string
    reference_string = input("Enter the reference string (space-separated integers): ")
    pages = [int(x) for x in reference_string.strip().split()]
    
    # Initialize variables
    frames = []  # List to store current pages in memory
    page_faults = 0
    next_position = 0  # Position to replace in FIFO order
    
    print("\nFIFO Page Replacement Simulation:")
    print("-" * 50)
    
    # Process each page in the reference string
    for i, page in enumerate(pages):
        page_fault = False
        
        # Check if page is already in memory (page hit)
        if page not in frames:
            page_fault = True
            page_faults += 1
            
            # If frames list is not full, add the page
            if len(frames) < num_frames:
                frames.append(page)
            else:
                # Replace the oldest page (FIFO)
                frames[next_position] = page

                # move the pointer to the next position in a cycle
                # so that always pointed to the oldest page
                next_position = (next_position + 1) % num_frames
        
        # Print current state
        status = "Page fault" if page_fault else "Page hit"
        print(f"Step {i+1}: Reference page {page} → {frames} ({status})")
    
    # Print final results
    print("-" * 50)
    print(f"Total number of page faults: {page_faults}")
    print(f"Page fault rate: {page_faults/len(pages):.2%}")
    print(f"Page hit rate: {(len(pages) - page_faults)/len(pages):.2%}")

if __name__ == "__main__":
    fifo_page_replacement()
