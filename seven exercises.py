'''
Re‐write the fizz_buzz function to prompt a user to enter a
number and then return the function result.
'''

def fizz_buzz(x):
	if x % 3 == 0 and x % 5 == 0:
		print(f"{x} is Fizz Buzz!") 
	elif x % 3 == 0:
		print(f"{x} is Fizz")
	elif x % 5 == 0:
		print(f"{x} is Buzz")
	else:
		print(f"{x} is Boaring") 

num = input("Please enter a number: ")
fizz_buzz (int(num))

'''
Write some code using the same fizz_buzz function but have it
print out all numbers between 1 and 100 by calling the function
100 times.
'''
for num in range(1,100):
	fizz_buzz(num)


'''
 Create a function that has 7 things passed to it
'''
def seven_arg(a, b, c, d, e, f, g):
	print(f"A = {a}")
	print(f"B = {b}")
	print(f"C = {c}")
	print(f"D = {d}")
	print(f"E = {e}")
	print(f"F = {f}")
	print(f"G = {g}")

seven_arg(1, 2, 3, 4, 5, 6, 7)

'''
Create a function that asks a persons name, allows them to enter
the name, and then prints out a welcome message with that
name.
'''
def name_msg ():
	name = input("What is your name: ")
	print(f"Welcome to our training {name}")

name_msg()