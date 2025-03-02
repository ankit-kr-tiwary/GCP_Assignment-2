import multiprocessing
import time
import math

def stress_cpu():
    """Function to perform CPU-intensive calculations"""
    while True:
        _ = math.factorial(100000)  # Heavy computation to keep CPU busy

if __name__ == "__main__":
    num_cores = multiprocessing.cpu_count()  # Get total available CPU cores
    print(f"Starting stress test on {num_cores} CPU cores...")

    processes = []
    for _ in range(num_cores):  # Use all CPU cores
        p = multiprocessing.Process(target=stress_cpu)
        p.start()
        processes.append(p)

    try:
        time.sleep(300)  # Run for 5 minutes (adjust as needed)
    except KeyboardInterrupt:
        print("Stopping stress test...")
    finally:
        for p in processes:
            p.terminate()
