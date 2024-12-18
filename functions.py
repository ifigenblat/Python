'''
FUNCTIONS

def name(arguments):
    do stuff
'''
import math

def wisdom():
	print("You have to know when to hold em")

wisdom()

def fizz_buzz(x):
	if x % 3 == 0 and x % 5 == 0:
		print(f"{x} is Fizz Buzz!") 
	elif x % 3 == 0:
		print(f"{x} is Fizz")
	elif x % 5 == 0:
		print(f"{x} is Buzz")
	else:
		print(f"{x} is Boaring") 

fizz_buzz(97)

# RETURNING TRUE OR FALSE
def is_even(x):
	if x % 2 == 0:
		return True
	else:
		return False

print(is_even(99))

# ASSIGNING FUNCTION OUTPUT TO A VARIABLE
def is_even(x):
	if x % 2 == 0:
		return True
	else:
		return False

my_variable = is_even(99)
print(my_variable)

# FUNCTIONS CAN HAVE MORE THAN ONE ARGUMENT
def namer (first, last):
	print(f"Hello {first.capitalize()} {last.capitalize()}, nice to meet you!")

namer("john", "smith")

# USING DEFAULT ARGUMENTS
def namer(first = "John", last = "Smith"):
	print(f"First Name: {first}")
	print(f"Last Name: {last}")

namer()

#USING DEFAULT ARGUMENTS WHEN ONLY ONE ARGUMENT IS SENT
def namer(first = "John", last = "Smith"):
	print(f"First name: {first}")
	print(f"Last name: {last}")

namer("Itsik")

# USING DEFAULT ARGUMENTS WITH MATH
def performOperation(num1, num2, operation='sum'):
	if operation == 'sum':
		return num1 + num2
	if operation == 'multiply':
		return num1 * num2


print(f'{performOperation(2, 3)}')

# Keyword arguments must come after positional arguments
# Afterwards, keyword arguments can be in any oreder 

def performOperation(num1, num2, operation='sum', message='default message'):
	print(message)
	if operation == 'sum':
		return num1 + num2
	if operation == 'multiply':
		return num1 * num2


print(f'{performOperation(2, 3, message = 'new message', operation = 'multiply')}')

# Anticipate all the variables the user might be passing in
# *args - only works for positional arguments. Do not support keyword arguments

def performOperation(*args):
	print(args)

performOperation(1,2,3)

# **kwargs
def performOperation(*args, **kwargs):
	print(args)
	print(kwargs)

performOperation(1,2,3, operation = 'sum')


# rewrite for ultimate flexibility 
def performOperation(*args, operation = 'sum'):
	if operation == 'sum':
		return math.sum(args)
	if operation == 'multiply':
		return math.prod(args)

print(f'{performOperation(2, 3, 6, 7, 8, operation = 'multiply')}')


# VARIABLES AND SCOPE 
# local scope takes precedence over global scope

# locals() - return dctionary with all local variables 

def performOperation(*args, **kwargs):
	print(locals())

performOperation(2, 3, 6, 7, 8, operation = 'multiply')

# globals() - return dctionary with all global variables 

message = 'Some global data'
varA = 2
def function1(varA, varB):
	print(varA)
	print(message)
	print(locals())

def function2(varC, varB):
	print(varA)
	print(message)
	print(locals())	

function1(1,2)
function2(3,4)

# Inner function

def function1(varA, varB):
	message = 'Some local data'
	print(varA)
	def inner_function(varA, varB):
		print(f'inner_function local scope: {locals()}')
	print(locals())
	inner_function(123,456)
function1(1,2)

'''
Lambda functions - define a small function without a variable name (no function name)
Lambda functions - Convenient way to write "mini functions" as values 
'''

(lambda x: x + 3)
print( (5))

myList = [5,4,3,2]
print(sorted(myList))

myList = [{'num' : 3}, {'num' : 2}, {'num' : 1}]
print(sorted(myList, key=lambda x: x['num'] ))

