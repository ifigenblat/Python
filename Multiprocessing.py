# install multiprocess using pip install multiprocess

from multiprocessing import Process
import time
#import threading

def longSquare(num, results):
    time.sleep(1)
    print(num**2)
    print('Finished computing!')

if __name__ == "__main__": 
# Ensure that certain parts of the code are executed only when the script is run directly
# and not when it is imported as a module into another script.
# In some operating systems (like Windows), each new process spawns its own Python interpreter.
# Without if __name__ == "__main__":, the interpreter might recursively re-import the script, 
# causing infinite loops or errors. This check prevents those issues.
	results = {}
	processes = [Process(target=longSquare, args=(n, results)) for n in range(10)]

	# Start and join processes
	[p.start() for p in processes]
	[p.join() for p in processes]



'''
# Another solution to solve multiprocess does not share memory by default
# In multiprocess, each process gets its own memory space. 
# The results dictionary passed to the longSquare function is not shared across processes, 
# so each process gets its own copy of results, 
# and changes made inside a process won't reflect in the parent process.

# Solution: Use a shared object, such as a multiprocessing.Manager dictionary, 
# for inter-process communication.

from multiprocessing import Process, Manager
import time

def longSquare(num, results):
    time.sleep(1)
    square = num ** 2
    print(f"{num} squared is {square}")
    results[num] = square
    print("Finished computing!")

if __name__ == "__main__":
    manager = Manager()  # Shared memory manager
    results = manager.dict()  # Shared dictionary

    processes = [Process(target=longSquare, args=(n, results)) for n in range(10)]

    # Start and join processes
    [p.start() for p in processes]
    [p.join() for p in processes]

    # Print results after all processes finish
    print("Results:", dict(results))
'''