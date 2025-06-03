import threading
import time
import random

class DiningPhilosophers:
    def __init__(self, num_philosophers=5):
        self.num_philosophers = num_philosophers
        # Create 5 chopsticks as locks
        self.chopsticks = [threading.Lock() for _ in range(num_philosophers)]
        self.running = True
        self.philosophers = []
        
    def philosopher(self, phil_id):
        """Philosopher behavior with ordered chopstick pickup"""
        display_id = phil_id + 1
        while self.running:
            # Think
            print(f"Philosopher {display_id} is thinking...")
            time.sleep(random.uniform(1, 2))
            
            if not self.running:
                break
                
            # Get hungry and identify chopsticks
            left_chopstick = phil_id
            right_chopstick = (phil_id + 1) % self.num_philosophers
            
            print(f"Philosopher {display_id} is hungry and wants to eat")
            
            # DEADLOCK PREVENTION: Always pick up lower numbered chopstick first
            first_chopstick = min(left_chopstick, right_chopstick)
            second_chopstick = max(left_chopstick, right_chopstick)

            display_first = first_chopstick + 1
            display_second = second_chopstick + 1
            
            print(f"Philosopher {display_id} is trying to pick up chopsticks {display_first} and {display_second}")
            
            # Pick up chopsticks in order using 'with' for automatic cleanup
            with self.chopsticks[first_chopstick]:
                print(f"Philosopher {display_id} picked up chopstick {display_first}")
                
                with self.chopsticks[second_chopstick]:
                    print(f"Philosopher {display_id} picked up chopstick {display_second}")
                    
                    # Eat
                    print(f"Philosopher {display_id} is eating...")
                    time.sleep(random.uniform(1, 2))
                    
                    print(f"Philosopher {display_id} finished eating and put down both chopsticks")
                    
            print(f"Philosopher {display_id} returned to thinking")
            print("-" * 50)
            
    def start_simulation(self, duration=20):
        
        # Create and start philosopher threads
        for i in range(self.num_philosophers):
            thread = threading.Thread(target=self.philosopher, args=(i,))
            thread.daemon = True
            self.philosophers.append(thread)
            thread.start()
            print(f"Philosopher {i+1} started")
        
        # Let simulation run for specified duration
        try:
            time.sleep(duration)
        except KeyboardInterrupt:
            print("\nSimulation interrupted by user")
        
        # Stop simulation
        self.running = False
        
        # Wait for all threads to finish
        time.sleep(1)  # Give threads time to finish current operations
        for i, thread in enumerate(self.philosophers):
            thread.join(timeout=2)
            if thread.is_alive():
                print(f"Note: Philosopher {i+1} is still finishing up")
        
        print("Simulation ended successfully!")

def main():
    print("DINING PHILOSOPHERS PROBLEM")
    print("===========================")
    print("Solution: Ordered Chopstick Pickup")
    print("Number of Philosophers: 5")
    print()
    
    # Get simulation duration
    try:
        duration = int(input("Enter simulation duration in seconds (default 15): ") or 15)
    except ValueError:
        print("Invalid input, using default duration of 15 seconds")
        duration = 15
    
    print(f"\nStarting simulation for {duration} seconds...")
    print("Press Ctrl+C to stop early\n")
    
    # Create and run simulation
    simulation = DiningPhilosophers(5)
    simulation.start_simulation(duration)

if __name__ == "__main__":
    main()
