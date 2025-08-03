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

#? Check if the thread is still alive after joining
print(t.is_alive())

# Start the thread
t.start()

#? Check if the thread is still alive after joining
# Here the timer works in parallel while the print statement is executed and the thread waits for the task to complete
print(t.is_alive())

# Wait for the thread to complete, ensuring the main program does not exit before the thread finishes
t.join()

#? Check if the thread is still alive after joining
print(t.is_alive())