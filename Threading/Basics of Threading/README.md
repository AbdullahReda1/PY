# Python Threading - Part 1: Basics

## 1. What is a Thread?

A **thread** is the smallest unit of execution within a process.

- Threads share the same memory space and data.
- They are "lightweight" compared to full processes.
- Multiple threads can run concurrently to improve responsiveness.

Use case example:

> Downloading a file while updating a GUI progress bar.

---

## 2. Threading vs Multiprocessing

| Feature              | Threading            | Multiprocessing      |
| -------------------- | -------------------- | -------------------- |
| Memory               | Shared               | Separate             |
| Overhead             | Low                  | Higher               |
| Performance (Python) | Better for I/O-bound | Better for CPU-bound |
| GIL Affected         | Yes                  | No                   |
| Best For             | I/O-bound tasks      | CPU-bound tasks      |

The **Global Interpreter Lock (GIL)** ensures that only one thread executes Python bytecode at a time. This limits CPU-bound performance for threads, but has little impact on I/O-bound tasks.

---

## 3. When to Use Threading

Use threading when:

- Waiting for **I/O** (disk, network, user input)
- Improving **UI responsiveness**
- Performing **background tasks**
- Polling **sensors or hardware**

Avoid threading when:

- Performing **heavy numerical computations** (use `multiprocessing`)

---

## 4. Creating Threads in Python

Python’s `threading.Thread` class is used to create and manage threads.

There are two ways:

1. Pass a function to `Thread`
2. Subclass `Thread` and override `run()`
