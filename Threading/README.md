# Understanding the **API surface of the `threading` module:**

## 📦 Core Classes

| Class                          | Description                                                             |
| ------------------------------ | ----------------------------------------------------------------------- |
| `threading.Thread`             | Represents an individual thread of control                              |
| `threading.Lock`               | A basic lock object used for mutual exclusion (mutex)                   |
| `threading.RLock`              | A reentrant lock that can be acquired multiple times by the same thread |
| `threading.Semaphore`          | Allows a fixed number of threads to access a resource                   |
| `threading.BoundedSemaphore`   | Like `Semaphore` , but raises an error if released too many times       |
| `threading.Event`              | Used for signaling between threads                                      |
| `threading.Condition`          | More advanced synchronization (wait/notify)                             |
| `threading.Barrier`            | Synchronizes a fixed number of threads at a point                       |
| `threading.Timer`              | A thread that runs a function after a delay                             |
| `threading.local()`            | Creates thread-local storage (each thread has its own copy of data)     |

## 🔧 Thread Class Methods & Attributes

| Method/Attribute        | Description                                                      |
| ----------------------- | ---------------------------------------------------------------- |
| `.start()`              | Starts the thread                                                |
| `.run()`                | What the thread will do (you override it when subclassing)       |
| `.join(timeout=None)`   | Blocks until the thread finishes (or until `timeout`)            |
| `.is_alive()`           | Returns `True` if the thread is running                          |
| `.daemon`               | If `True` , thread is a daemon (auto-stops with main program)    |
| `.name`                 | Gets/sets the thread’s name                                      |
| `.ident`                | Unique ID assigned by Python to the thread                       |
| `.native_id`            | OS-level thread ID (Python 3.8+)                                 |

## 🧵 Module-Level Functions

| Function                       | Description                                 |
| ------------------------------ | ------------------------------------------- |
| `threading.current_thread()`   | Returns the current `Thread` object         |
| `threading.active_count()`     | Number of currently active threads          |
| `threading.enumerate()`        | List of all active threads                  |
| `threading.main_thread()`      | Returns the main thread object              |
| `threading.get_ident()`        | Thread identifier of the current thread     |
| `threading.get_native_id()`    | OS thread ID (Python 3.8+)                  |
| `threading.settrace(func)`     | Set a global trace function for all threads |
| `threading.setprofile(func)`   | Set profiling function for all threads      |

## 🔒 Lock Classes (for synchronization)

| Class/Method                                | Description                                                     |
| ------------------------------------------- | --------------------------------------------------------------- |
| `Lock.acquire(blocking=True, timeout=-1)`   | Lock the resource                                               |
| `Lock.release()`                            | Unlock the resource                                             |
| `RLock.acquire()`                           | Like `Lock` but reentrant (can lock again in the same thread)   |
| `RLock.release()`                           | Releases a reentrant lock                                       |
| `with threading.Lock()`                     | Context manager for auto-locking/unlocking                      |

## 🎯 Event Methods

| Method                  | Description                                            |
| ----------------------- | ------------------------------------------------------ |
| `.set()`                | Set the flag to `True` (signals all waiting threads)   |
| `.clear()`              | Resets the flag to `False`                             |
| `.wait(timeout=None)`   | Blocks until `.set()`                                  |
| `.is_set()`             | Returns `True` if the internal flag is `True`          |

## 🧱 Condition Methods

| Method                          | Description                                 |
| ------------------------------- | ------------------------------------------- |
| `.acquire()` / `.release()`     | Lock the condition variable.                |
| `.wait(timeout=None)`           | Wait for `.notify()` or `.notify_all()`     |
| `.notify()`                     | Wake up one waiting thread                  |
| `.notify_all()`                 | Wake up all waiting threads                 |

## 🧭 Timer Class

| Method                                                          | Description                                               |
| --------------------------------------------------------------- | --------------------------------------------------------- |
| `threading.Timer(interval, function, args=None, kwargs=None)`   | Run a function after `interval` seconds in a new thread   |
| `.start()`                                                      | Start the timer                                           |
| `.cancel()`                                                     | Cancel the timer if still waiting                         |

## 🏷️ Constants / Macros

| Argument              | Description                                        |
| ----------------------| -------------------------------------------------- |
| `daemon=True/False`   | Set when creating or before starting the thread    |
| `target`              | Function to be executed in the thread              |
| `args=()`             | Tuple of arguments to pass to the target function  |
| `kwargs={}`           | Dictionary of keyword args for the target function |
| `name="..."`          | Optional name for the thread                       |
