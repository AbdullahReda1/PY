# impotint threading and time modules
import threading
import time

# Defining a class that inherits from threading.Thread
class MyThread(threading.Thread):
    # This method must be overridden with run method so that it can be executed when the thread starts.
    # if not overridden with run method, it will not be executed by the thread.
    def run(self):
        # A simple method that simulates work by sleeping for 2 seconds.
        print("Thread started")
        time.sleep(2)
        print("Thread finished")

# Create an instance of MyThread class to create a object of the thread class
t = MyThread()

# Start the thread
t.start()

# Wait for the thread to complete, ensuring the main program does not exit before the thread finishes
t.join()