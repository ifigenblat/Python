'''
FUNCTIONS

def name(arguments):
    do stuff
'''
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