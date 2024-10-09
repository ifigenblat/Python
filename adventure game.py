import os
from os import system
if os.name == 'nt': 
	clear = "cls"
else: 
	clear = "clear"
print("Welcome to choose your own Adventure!")
print("The goal is to find the Python princess...")
name = input("Enter you name: ")
name = name.lower()
system(clear)
print("You're standing in front of two doors...")
print("Do you want the door on the left or right?")
question = input().lower()
if question == "left":
	system(clear)
	print("You fell into a pit and died! GAVE OVER")
elif question == "right":
	system(clear)
	print(f"congratulations {name.capitalize()} you found")
	print("the python princess! YOU WIN!")
else:
	system(clear)
	print("Sorry, I don't recognize your response GAME OVER")