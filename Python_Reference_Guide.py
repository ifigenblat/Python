# Python Reference Guide
#Need a quick reference guide to help you while you hack? This is no substitute for the actual course content, but here's a "cheatsheet" to help jog your memory!
## Handy Functions
print('This will print some text')
# Use string formatting ("f-strings") to insert values
name = 'Ryan'
f'My name is: {name}'
# An iterable object containing sequential integers
range(0, 10)

# Iterate by steps of 2
range(0, 10, 2)
# Returns the datatype of the value passed in
type(1)
## Math Operators
# Addition
1 + 1
# Subtraction
2 - 1
# Multiplication
5 * 5
# Division
25 / 5
# Exponents 
5 ** 3
# Modulus (remainder after division)
17 % 5
## Data Types
# Integers
x = 1
type(x)
# Floats
x = 1.0
type(x)
# Strings
x = 'Ryan'
type(x)
# Booleans
x = True
type(x)
# Byte data
x = bytes(4)
type(x)
### Casting Datatypes
# String to integer
int('1')
# Float to integer
int(1.5)
# Integer to float
float(1)
# Integer to boolean
bool(1)
# String to boolean (Anything other than an empty string is True)
bool('')
# Int to string
str(1)
# String to bytes, requires the encoding
bytes('🙂', 'utf-8')
## String Operators
# String concatenation
'Ryan ' + 'Mitchell'
# String multiplication
'Python'*6
# Access a particular character in a string
'Python'[3]
## Boolean Operators
# AND
print(True and True)
print(True and False)
print(False and False)
# OR
print(True or True)
print(True or False)
print(False or False)
# NOT 
print(not True)
print(not False)
# Equality operator
5 == 5
# Inequality operator
5 != 4
# Less than
4 < 5
# Less than or equals to 
5 <= 5
# Greater than
5 > 4
# Greater than or equals to
5 >= 5
## Control Flow

if False: 
    print('This does not print')
else: 
    print('This will print')
# Iterate through items in a range
for i in range(0, 5):
    print('Number: {}'.format(i))
# Iterate through items in a list
for i in [1,2,3,4,5]:
    print('Number: {}'.format(i))
i = 0
while i < 5:
    print('Number: {}'.format(i))
    i = i + 1
## Data Types
### Lists
aList = [1,2,3,4]
type(aList)
# Append item to a list
aList.append(5)
aList
# List concatenation
[1,2,3] + [4,5,6]
# List multiplication
[1,2] * 5
# Accessing items in a list

aList = [1,2,3,4,5,6,7,8,9,10]
# Print the item at index 4
print(aList[4])

# Print the items at index 0, up to (not including) index 4
print(aList[0:4])

# If the first index is missing, it's assumed to be 0
print(aList[:4])

# If the last index is missing, it's assumed to go to the end of the list
print(aList[4:])

# Print every other item in the list
print(aList[::2])

# Print every third item in the list
print(aList[::3])
### Dictionaries
aDict = {
    'one': 1,
    'two': 2,
    'three': 3,
}
# Add key/value pairs to dictionary
aDict['four'] = 4

# Access values by keys
print(aDict['one'])
# Print all keys
print(aDict.keys())

# Print all values
print(aDict.values())

# Print all key/value pairs
print(aDict.items())
### Sets
aSet = {1,2,3,4}

# Add an item to a set
aSet.add(5)

# Remove an item from a set
aSet.remove(2)
print(aSet)
### Tuples
# Tuples cannot be modified
aTuple = (1,2,3,4)
aTuple
## Functions
# Function with one argument and a return value
def aFunction(anArg):
    return anArg + 1

aFunction(5)
# Different ways of calling a function with a keyword argument
def aFunction(anArg, optionalArg=1):
    return anArg + optionalArg

print(aFunction(5))
print(aFunction(5, 4))
print(aFunction(5, optionalArg=4))
## Classes
# A simple class with one attribute and one method
class ParentClass:
    def __init__(self, val):
        self.val = val
        
    def printVal(self):
        print(self.val)
        

classInstance = ParentClass('Value for the class attribute "val"')
classInstance.printVal()
# Extend the parent class to create a child class        
class ChildClass(parentClass):
    
    def printVal(self):
        print('Child class! {}'.format(self.val))
        
childInstance = ChildClass('Value for the class attribute "val"')
childInstance.printVal()   
# Overriding the parent class constructor
class AnotherChildClass(parentClass):
    def __init__(self):
        super().__init__('A default value')
        
anotherChildInstance = AnotherChildClass()
anotherChildInstance.printVal()
## File Handling
# Open a file for reading
with open('09_01_file.txt', 'r') as f:
    data = f.readlines()
print(data)
with open('test.txt', 'w') as f:
    f.write('Writing a new line\n')
with open('test.txt', 'a') as f:
    f.write('Adding a new line to the last one\n')