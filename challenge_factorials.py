'''
Factorial: n! = n * (n-1) * (n-2) *...*3 *2 *1 
Examples: 
5! = 5 * 4 * 3 * 2 * 1 = 120 
6! = 6 * 5 * 4 * 3 * 2 * 1 = 720

Write a function called factorial that returns the factorial of a number passed in.
if the number pass in is 0 or positve integer the function should return the factorial, 
if it's not one of these, the funtion should return "None"

Mathematicians have decided that in a set of 0 items (en empty set) there is only one way to arrange them, therefore:
0! = 1 
'''


def get_factorial(num):
	if str(num).isnumeric():
		number = int(num)
		if number >= 0:
			i = number
			if number > 0:
				while i > 1:
					i = i - 1
					number = number * i
					return number
			else:
				return 1
		else:
			return None
	else:
		return None

def factorial (num):
	if type(num) != int:
		return None
	if num < 0:
		return None

	fact = 1
	counter = 1
	while counter <= num:
		fact = fact * counter
		counter = counter + 1
	return fact

number = input("What number you would like to get the factorial for? ")

result = get_factorial(number)
print(f"{result}")

#number = 5
#result = factorial(number)
#print(f"{result}")