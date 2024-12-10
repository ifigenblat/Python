'''
List
Definition: An ordered, mutable collection of items, which can contain elements of different types.
'''
#Declaration:
my_list = [1, 2, 3, "apple", 4.5]

# Example:
# Creating a list
fruits = ["apple", "banana", "cherry"]

# Appending an item
fruits.append("date")

# Accessing elements
print(fruits[1])  # Output: banana

# Modifying an element
fruits[2] = "citrus"

print(fruits)  # Output: ['apple', 'banana', 'citrus', 'date']
'''
Limitations:
* Slower for operations like insertions and deletions in large lists (due to shifting elements).
* Consumes more memory due to dynamic resizing.
'''

'''
Tuple
Definition: An ordered, immutable collection of items.
'''
#Declaration:
my_tuple = (1, 2, 3, "apple", 4.5)

# Example:
# Creating a tuple
coordinates = (10.0, 20.0)

# Accessing elements
print(coordinates[0])  # Output: 10.0

# Attempting to modify (will raise an error)
try:
    coordinates[1] = 30.0
except TypeError as e:
    print(e)  # Output: 'tuple' object does not support item assignment
'''
Limitations:
* Immutable, so elements cannot be changed or modified once defined.
* Less flexible for use cases requiring frequent updates.
'''

'''
Dictionary
Definition: A collection of key-value pairs, where keys are unique, and values can be of any data type.
'''
# Declaration:
my_dict = {"name": "Alice", "age": 30, "city": "New York"}

# Example:
# Creating a dictionary
student = {
    "name": "John Doe",
    "age": 21,
    "courses": ["Math", "Science"]
}

# Accessing a value by key
print(student["name"])  # Output: John Doe

# Adding a new key-value pair
student["graduated"] = False

# Iterating over keys and values
for key, value in student.items():
    print(f"{key}: {value}")

'''
Limitations:
Keys must be hashable (e.g., lists cannot be used as keys).
Unordered before Python 3.7 (in Python 3.7+, dictionaries maintain insertion order).
'''

'''
Set
Definition: An unordered collection of unique items.
'''
# Declaration:
my_set = {"apple", "banana", "cherry"}
# Example:
# Creating a set
fruits = {"apple", "banana", "cherry"}

# Adding an item
fruits.add("date")

# Attempting to add a duplicate (ignored)
fruits.add("apple")

print(fruits)  # Output: {'banana', 'cherry', 'date', 'apple'}

# Removing an item
fruits.remove("banana")

print(fruits)  # Output: {'cherry', 'date', 'apple'}

# Set operations
set_a = {1, 2, 3}
set_b = {3, 4, 5}

print(set_a.union(set_b))      # Output: {1, 2, 3, 4, 5}
print(set_a.intersection(set_b))  # Output: {3}
'''
Limitations:
* Unordered, so no indexing or slicing.
* Cannot contain duplicate elements.
'''

'''
Frozenset
Definition: An immutable version of a set.
'''
# Declaration:
my_frozenset = frozenset(["apple", "banana", "cherry"])

# Example:
# Creating a frozenset
fruits = frozenset(["apple", "banana", "cherry"])

# Attempting to add an item (will raise an error)
try:
    fruits.add("date")
except AttributeError as e:
    print(e)  # Output: 'frozenset' object has no attribute 'add'

# Set operations
set_a = frozenset([1, 2, 3])
set_b = frozenset([3, 4, 5])

print(set_a.union(set_b))      # Output: frozenset({1, 2, 3, 4, 5})
print(set_a.intersection(set_b))  # Output: frozenset({3})
'''
Limitations:
* Cannot add or remove elements once created.
* Still unordered and does not allow duplicates.

'''
'''
String
Definition: An immutable sequence of characters.
'''
# Declaration:
my_string = "Hello, World!"

# Example:
# Creating a string
greeting = "Hello, World!"

# Accessing characters
print(greeting[7])  # Output: W

# Slicing
print(greeting[:5])  # Output: Hello

# Attempting to modify (will raise an error)
try:
    greeting[0] = "h"
except TypeError as e:
    print(e)  # Output: 'str' object does not support item assignment

# Concatenation
new_greeting = greeting + " How are you?"
print(new_greeting)  # Output: Hello, World! How are you?
'''
Limitations:
* Cannot modify the content directly (must create a new string).
* perations like concatenation are memory-intensive due to immutability.
'''

'''
Byte and Bytearray
	
	* Byte
		Definition: An immutable sequence of bytes.
'''
# Declaration:
my_bytes = b"Hello"

# Example:
# Creating bytes
data = b"Hello"

# Accessing elements
print(data[1])  # Output: 101 (ASCII value of 'e')

# Attempting to modify (will raise an error)
try:
    data[0] = 104
except TypeError as e:
    print(e)  # Output: 'bytes' object does not support item assignment

'''
	* Bytearray
		Definition: A mutable sequence of bytes.
'''

# Declaration:
my_bytearray = bytearray("Hello", "utf-8")

# Example:
# Creating a bytearray
data = bytearray("Hello", "utf-8")

# Modifying elements
data[0] = 104  # 'h' in ASCII
print(data)  # Output: bytearray(b'hello')

# Appending bytes
data.append(33)  # '!' in ASCII
print(data)  # Output: bytearray(b'hello!')
'''
Limitations:
* Limited to handling binary data.
* Does not support operations meant for higher-level data structures.

Range
Definition: A sequence of numbers generated lazily, often used in loops.
Declaration:
python
Copy code
my_range = range(0, 10, 2)  # start=0, stop=10, step=2
Example:
python
Copy code
# Creating a range
numbers = range(1, 5)

# Iterating through a range
for num in numbers:
    print(num)

# Output:
# 1
# 2
# 3
# 4

# Accessing elements by index
print(numbers[2])  # Output: 3

# Attempting to modify (range is immutable)
try:
    numbers[0] = 10
except TypeError as e:
    print(e)  # Output: 'range' object does not support item assignment
Limitations:
Cannot directly modify or add to the range.
Suitable only for numerical sequences.
9. Deque (Double-Ended Queue)
Definition: A list-like container optimized for fast appends and pops from both ends.
Declaration:
python
Copy code
from collections import deque
my_deque = deque([1, 2, 3])
Example:
python
Copy code
from collections import deque

# Creating a deque
dq = deque(["left", "middle", "right"])

# Appending to both ends
dq.append("new_right")
dq.appendleft("new_left")

print(dq)  # Output: deque(['new_left', 'left', 'middle', 'right', 'new_right'])

# Popping from both ends
right = dq.pop()
left = dq.popleft()

print(right)  # Output: new_right
print(left)   # Output: new_left
print(dq)     # Output: deque(['left', 'middle', 'right'])

# Accessing elements
print(dq[1])  # Output: middle
Limitations:
Less efficient for random access compared to lists.
Requires importing the collections module.
10. Stack
Definition: A LIFO (Last In, First Out) data structure, often implemented using lists or the collections.deque.
Declaration (Using List):
python
Copy code
stack = []
Example:
python
Copy code
# Implementing a stack with a list
stack = []

# Pushing items
stack.append('first')
stack.append('second')
stack.append('third')

print(stack)  # Output: ['first', 'second', 'third']

# Popping items
last = stack.pop()
print(last)    # Output: third
print(stack)   # Output: ['first', 'second']

# Peek at the top item
top = stack[-1]
print(top)     # Output: second
Limitations:
Using lists for stacks can be inefficient due to memory overhead.
Deque implementation does not support random access.
11. Queue
Definition: A FIFO (First In, First Out) data structure, implemented using the queue.Queue or collections.deque.

Declaration (Using queue.Queue):

python
Copy code
from queue import Queue
q = Queue()
Example (Using queue.Queue):

python
Copy code
from queue import Queue

# Creating a queue
q = Queue()

# Enqueue items
q.put('first')
q.put('second')
q.put('third')

# Dequeue items
first_item = q.get()
print(first_item)  # Output: first

second_item = q.get()
print(second_item)  # Output: second

print(q.empty())  # Output: False
Example (Using collections.deque):

python
Copy code
from collections import deque

# Creating a deque as a queue
q = deque()

# Enqueue items
q.append('first')
q.append('second')
q.append('third')

# Dequeue items
first_item = q.popleft()
print(first_item)  # Output: first

second_item = q.popleft()
print(second_item)  # Output: second

print(len(q))  # Output: 1
Limitations:

Standard queue.Queue can be slower compared to deque for small-scale use.
deque lacks thread-safety features.
12. Heap
Definition: A binary heap for priority queues, implemented using the heapq module.
Declaration:
python
Copy code
import heapq
heap = []
Example:
python
Copy code
import heapq

# Creating a heap
heap = []

# Adding elements
heapq.heappush(heap, 3)
heapq.heappush(heap, 1)
heapq.heappush(heap, 4)
heapq.heappush(heap, 2)

print(heap)  # Output: [1, 2, 4, 3]

# Popping the smallest element
smallest = heapq.heappop(heap)
print(smallest)  # Output: 1
print(heap)      # Output: [2, 3, 4]

# Converting a list into a heap
numbers = [5, 7, 9, 1, 3]
heapq.heapify(numbers)
print(numbers)  # Output: [1, 3, 9, 7, 5]
Limitations:
Not a complete queue—requires manual management of elements.
Lacks threading support.
13. Linked List (Custom Implementation Required)
Definition: A linear collection of nodes where each node points to the next. Must be implemented manually.
Declaration:
python
Copy code
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
Example:
python
Copy code
# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None
    
    # Append a new node
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
    
    # Print the list
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Using the LinkedList
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.print_list()  # Output: 1 -> 2 -> 3 -> None
Limitations:
Not natively supported in Python.
Slower than lists for direct indexing.
14. Graph (Custom Implementation or Using Libraries)
Definition: A collection of nodes (vertices) and edges, used to represent networks.
Declaration (Using networkx Library):
python
Copy code
import networkx as nx
G = nx.Graph()
Example:
python
Copy code
import networkx as nx
import matplotlib.pyplot as plt

# Creating a graph
G = nx.Graph()

# Adding nodes
G.add_node("A")
G.add_node("B")
G.add_node("C")

# Adding edges
G.add_edge("A", "B")
G.add_edge("B", "C")
G.add_edge("C", "A")

# Drawing the graph
nx.draw(G, with_labels=True)
plt.show()

# Accessing neighbors
print(list(G.neighbors("A")))  # Output: ['B', 'C']
Limitations:
Requires external libraries (e.g., networkx) for efficient and complex operations.
Can become memory-intensive with large graphs.
15. Matrix
Definition: A 2D array or list of lists used to represent tabular data. For advanced operations, numpy arrays are preferred.

Declaration (Using List of Lists):

python
Copy code
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
Example:

python
Copy code
# Creating a matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Accessing elements
print(matrix[0][1])  # Output: 2

# Iterating through the matrix
for row in matrix:
    for element in row:
        print(element, end=" ")
    print()

# Output:
# 1 2 3 
# 4 5 6 
# 7 8 9 
Declaration (Using numpy):

python
Copy code
import numpy as np
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
Example (Using numpy):

python
Copy code
import numpy as np

# Creating a numpy matrix
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# Accessing elements
print(matrix[0, 1])  # Output: 2

# Matrix operations
print(matrix + 1)
# Output:
# [[2 3 4]
#  [5 6 7]
#  [8 9 10]]

print(np.transpose(matrix))
# Output:
# [[1 4 7]
#  [2 5 8]
#  [3 6 9]]
Limitations:

Pure Python implementation lacks efficiency.
Requires numpy or similar libraries for high performance.
16. Frozen Dictionary (Not Built-In, Requires External Libraries)
Definition: An immutable version of a dictionary.
Declaration (Using types.MappingProxyType):
python
Copy code
from types import MappingProxyType
my_dict = {"name": "Alice", "age": 30}
frozen_dict = MappingProxyType(my_dict)
Example:
python
Copy code
from types import MappingProxyType

# Creating a regular dictionary
original = {"key1": "value1", "key2": "value2"}

# Creating a frozen dictionary
frozen = MappingProxyType(original)

print(frozen["key1"])  # Output: value1

# Attempting to modify (will raise an error)
try:
    frozen["key1"] = "new_value"
except TypeError as e:
    print(e)  # Output: 'mappingproxy' object does not support item assignment

# Modifying the original dictionary affects the frozen dictionary
original["key1"] = "new_value"
print(frozen["key1"])  # Output: new_value
Limitations:
Requires manual implementation or external libraries.
Read-only access to keys and values.
'''