import random
from os import system
from fractions import Fraction
# function to start the game and pick cards

global_user_right = 0
global_user_wrong = 0

def start_game():
	system("clear") # clear the screen  
	global global_user_right
	global global_user_wrong

# resetting global count to 0
	global_user_right = 0
	global_user_wrong = 0 

	print("welcome to Math flashcard! ")
	pick = input("Choose your falshcard (add|subtract|multiply|divide|fraction): ")
	flashcards(pick.lower())
	print(f"You answered {global_user_right} questions right!, and {global_user_wrong} questions wrong!")

# start function flashcards
def flashcards(pick):
    system("clear")
    
    if pick == "fraction":
    	# Generate two random fractions
    	card_one = Fraction(random.randint(1, 10), random.randint(1, 10))
    	card_two = Fraction(random.randint(1, 10), random.randint(1, 10))
    else:
    	card_one = random.randint(1,10)
    	card_two = random.randint(1,10)

    # proceeding according to user selection
    # Add
    if pick == "add":
    	correct = card_one + card_two
    	answer = input(f"{card_one} + {card_two} = ")
    	if int(answer) == correct:
    		print(f"Correct! {card_one} + {card_two} = {answer}")
    		keep_track(True)
    	else:
        	print(f"Wrong! {card_one} + {card_two} = {correct}")
        	keep_track(False)
    # fraction
    elif pick == "fraction":
    	correct = card_one + card_two
    	answer = input(f"{card_one} + {card_two} = ")
    	if Fraction(answer) == correct:
    		print(f"Correct! {card_one} + {card_two} = {answer}")
    		keep_track(True)
    	else:
    		print(f"Wrong! {card_one} + {card_two} = {correct}")
    		keep_track(False)
    # Multiply
    elif pick == "multiply":
    	correct = card_one * card_two
    	answer = input(f"{card_one} * {card_two} = ")
    	if int(answer) == correct:
    		print(f"Correct! {card_one} * {card_two} == {answer}")
    		keep_track(True)
    	else:
    		print(f"Wrong! {card_one} * {card_two} = {correct}")
    		keep_track(False)
    # Subtract
    elif pick == "subtract":
    	correct = card_one - card_two
    	answer = input(f"{card_one} - {card_two} = ")
    	if int(answer) == correct:
    		print(f"Correct! {card_one} - {card_two} = {answer}")
    		keep_track(True)
    	else:
    		print(f"Wrong! {card_one} - {card_two} = {correct}")
    		keep_track(False)
    # Divide		
    elif pick == "divide":
    	correct = card_one / card_two
    	answer = input(f"{card_one} / {card_two} = ")
    	if float(answer) == correct:
    		print(f"Correct! {card_one} / {card_two} = {answer}")
    		keep_track(True)
    	else:
    		print(f"Wrong! {card_one} / {card_two} = {correct}")
    		keep_track(False)
    else:
    	print(f"Sorry, I don't recognize {pick}")
    	input("Please hit enter to try again")
    	start_game()
    # Ask if the user wants to continue
    play = input("Would you like another card? yes|no|restart: ")

    if play.lower() == "yes":
        flashcards(pick)
    elif play.lower() == "no":
        print("Thank you for playing!")
    elif play.lower() == "restart":
        start_game()
    else:
        print(f"Sorry, I don't recognize {play}")
        input("Please hit enter to try again. ")
        flashcards(pick)
# End function flashcards

# counting function for right and wrong answers
def keep_track(x):
	global global_user_right
	global global_user_wrong

	if x == True:
		global_user_right += 1
	else:
		global_user_wrong += 1
# End of tracking 

start_game()