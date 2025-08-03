# impotint threading and time modules
import threading
import time

# Define a simple method task to run in a thread
def task():
    # A simple task that simulates work by sleeping for 2 seconds.
    print("Thread started")
    time.sleep(2)
    print("Thread finished")

# Create a thread that runs the task method where target is the task function and Thread is the class from threading module
t = threading.Thread(target = task)

# Start the thread
t.start()

# Wait for the thread to complete, ensuring the main program does not exit before the thread finishes
t.join()