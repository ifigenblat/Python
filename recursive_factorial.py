# Factorial Recursive solution
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
def recursive_factorial(num):
	if type(num) != int:
		return None
	if num < 0:
		return None
	if num == 0:
		return 1
	return num * recursive_factorial(num - 1)

number = input("What number you would like to get the factorial for? ")

number = 5
result = recursive_factorial(number)
print(f"{result}")