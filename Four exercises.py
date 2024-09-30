'''
Create a simple math flashcard game that asks a user what two
numbers added together equal and tell them whether or not they
got the answer correct.
'''
from os import system
system("clear")
num_1 = 2
num_2 = 4
total = (num_1 + num_2)
results = int(input(f'How much is {num_1} + {num_2} ? '))
system("clear")
if results == total:
	print("You are correct!")
else:
	print("You are wrong!")

'''
Write some code that asks for a personʹs full name (first and last
name) and then output their name with both first and last name
capitalized
'''
name = input("please write your full name: ")
print(f'your full name is {name.title()}')

'''
Write some code that asks for a personʹs name and then tell that
person how many characters are in their name (added them up
manually yourself to see if the answer is correct!)
'''
first_name = input("What is your name? ")
print(f'Your name has {len(first_name)} characters.')