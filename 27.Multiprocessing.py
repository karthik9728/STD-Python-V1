from multiprocessing import Process
import os
import time

def show_info(name):
    print(f"Task '{name}' is running in process id: {os.getpid()}")
    time.sleep(2)
    print(f"Task '{name}' finished.")

if __name__ == "__main__":
    # On Windows, this guard is REQUIRED
    p1 = Process(target=show_info, args=("Job-1",))
    p2 = Process(target=show_info, args=("Job-2",))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Main process done.")