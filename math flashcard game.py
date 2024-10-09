
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

	global_user_right = 0
	global_user_wrong = 0 
	print("welcome to Math flashcard! ")
	pick = input("Choose your falshcard (add|subtract|multiply|divide|fraction): ")
	if pick.lower() == "add":
		print(f" You picked {pick}")
		add_flashcards()
		print(f"You answered {global_user_right} questions right!, and {global_user_wrong} questions wrong!")
	elif pick.lower() == "subtract":
		print(f" You picked {pick}")
		subtract_flashcards()
		print(f"You answered {global_user_right} questions right!, and {global_user_wrong} questions wrong!")
	elif pick.lower() == "multiply":
		print(f"You picked {pick}")
		multiply_flashcards()
		print(f"You answered {global_user_right} questions right!, and {global_user_wrong} questions wrong!")
	elif pick.lower() == "divide":
		print(f" You picked {pick}")
		divide_flashcards()
		print(f"You answered {global_user_right} questions right!, and {global_user_wrong} questions wrong!")
	elif pick.lower() == "fraction":
		print(f" You picked {pick}")
		fraction_flashcards()
		print(f"You answered {global_user_right} questions right!, and {global_user_wrong} questions wrong!")
	else:
		print(f"Sorry, I don't recognize {pick}")
		input("Please hit enter to try again")
		start_game()

# Start Addition Flashcards function
def add_flashcards():
	system("clear")
	card_one = random.randint(0,10)
	card_two = random.randint(0,10)
	correct = card_one + card_two
	answer = input(f"{card_one} + {card_two} = ")
	if int(answer) == correct:
		print(f"Correct! {card_one} + {card_two} = {answer}")
		keep_track(True)
	else:
		print(f"Wrong! {card_one} + {card_two} = {correct}")
		keep_track(False)
	play = input("Would you like anohter card? yes|no|restart: ")

	if play.lower() == "yes":
		add_flashcards()
	elif play.lower() == "no":
		print("Thank you for playing!")
	elif play.lower() == "restart":
		start_game()
	else:
		print(f"Sorry, I don't recognize {play}")
		input("Please hit enter to try again. ")
		add_flashcards()
	# End Addition Flashcards function	

# Start subtruct flashcards funtion
def subtract_flashcards():
	system("clear")
	card_one = random.randint(0,10)
	card_two = random.randint(0,10)
	correct = card_one - card_two
	answer = input(f"{card_one} - {card_two} = ")
	if int(answer) == correct:
		print(f"Correct! {card_one} - {card_two} = {answer}")
		keep_track(True)
	else:
		print(f"Wrong! {card_one} - {card_two} = {correct}")
		keep_track(False)
	play = input("Would you like anohter card? yes|no|restart: ")

	if play.lower() == "yes":
		subtract_flashcards()
	elif play.lower() == "no":
		print("Thank you for playing!")
	elif play.lower() == "restart":
		start_game()
	else:
		print(f"Sorry, I don't recognize {play}")
		input("Please hit enter to try again. ")
		subtract_flashcards()
	# End subtruct flashcards funtion

# Start multiply Flashcards function	
def multiply_flashcards():
	system("clear")
	card_one = random.randint(0,10)
	card_two = random.randint(0,10)
	correct = card_one * card_two
	answer = input(f"{card_one} * {card_two} = ")
	if int(answer) == correct:
		print(f"Correct! {card_one} * {card_two} = {answer}")
		keep_track(True)
	else:
		print(f"Wrong! {card_one} * {card_two} = {correct}")
		keep_track(False)
	play = input("Would you like anohter card? yes|no|restart: ")

	if play.lower() == "yes":
		multiply_flashcards()
	elif play.lower() == "no":
		print("Thank you for playing!")
	elif play.lower() == "restart":
		start_game()
	else:
		print(f"Sorry, I don't recognize {play}")
		input("Please hit enter to try again. ")
		multiply_flashcards()
	# End multiply Flashcards function	

# Start Addition Flashcards function
def divide_flashcards():
	system("clear")
	card_one = random.randint(0,10)
	card_two = random.randint(1,10)
	correct = card_one / card_two
	answer = input(f"{card_one} / {card_two} = ")
	if int(answer) == correct:
		print(f"Correct! {card_one} / {card_two} = {answer}")
		keep_track(True)
	else:
		print(f"Wrong! {card_one} / {card_two} = {correct}")
		keep_track(False)
	play = input("Would you like anohter card? yes|no|restart: ")

	if play.lower() == "yes":
		divide_flashcards()
	elif play.lower() == "no":
		print("Thank you for playing!")
	elif play.lower() == "restart":
		start_game()
	else:
		print(f"Sorry, I don't recognize {play}")
		input("Please hit enter to try again. ")
		divide_flashcards()
	# End Addition Flashcards function

def keep_track(x):
	global global_user_right
	global global_user_wrong

	if x == True:
		global_user_right += 1
	else:
		global_user_wrong += 1

def fraction_flashcards():
    system("clear")
    
    # Generate two random fractions
    card_one = Fraction(random.randint(1, 10), random.randint(1, 10))
    card_two = Fraction(random.randint(1, 10), random.randint(1, 10))
    
    # Correct answer in fraction form
    correct = card_one + card_two
    
    # Get user input
    answer = input(f"{card_one} + {card_two} = ")
    
    # Convert user input to a Fraction
    try:
        user_answer = Fraction(answer)
    except ValueError:
        print("Invalid input! Please enter a fraction in the form 'numerator/denominator'.")
        fraction_flashcards()
        return
    
    # Check if the answer is correct
    if user_answer == correct:
        print(f"Correct! {card_one} + {card_two} = {user_answer}")
        keep_track(True)
    else:
        print(f"Wrong! {card_one} + {card_two} = {correct}")
        keep_track(False)

    # Ask if the user wants to continue
    play = input("Would you like another card? yes|no|restart: ")

    if play.lower() == "yes":
        fraction_flashcards()
    elif play.lower() == "no":
        print("Thank you for playing!")
    elif play.lower() == "restart":
        start_game()
    else:
        print(f"Sorry, I don't recognize {play}")
        input("Please hit enter to try again. ")
        fraction_flashcards()

start_game()
