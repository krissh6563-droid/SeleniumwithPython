import time

def stopwatch():
    start_time = time.time()  # Get the current time when the stopwatch starts
    input("Press Enter to stop the stopwatch...")
    end_time = time.time()  # Get the current time when the stopwatch stops

    elapsed_time = end_time - start_time  # Calculate the elapsed time
    print(f"Elapsed time: {elapsed_time:.2f} seconds")

if __name__ == "__main__":
    print("Stopwatch started. Press Enter to stop.")
    stopwatch()
