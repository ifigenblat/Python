import random
from os import system
from fractions import Fraction

# Initialize global counters
global_user_right = 0
global_user_wrong = 0

def start_game():
    system("clear")
    global global_user_right, global_user_wrong
    global_user_right = 0
    global_user_wrong = 0 

    print("Welcome to Math Flashcard!")
    pick = input("Choose your flashcard (add|subtract|multiply|divide|fraction): ").lower()
    
    if pick in ["add", "subtract", "multiply", "divide", "fraction"]:
        print(f"You picked {pick}")
        flashcard_function = {
            "add": add_flashcards,
            "subtract": subtract_flashcards,
            "multiply": multiply_flashcards,
            "divide": divide_flashcards,
            "fraction": fraction_flashcards
        }[pick]
        flashcard_function()
    else:
        print(f"Sorry, I don't recognize {pick}")
        input("Please hit enter to try again.")
        start_game()

def ask_question(operation, card_one, card_two, correct):
    answer = input(f"{card_one} {operation} {card_two} = ")
    return int(answer) == correct

def add_flashcards():
    system("clear")
    card_one, card_two = random.randint(0, 10), random.randint(0, 10)
    correct = card_one + card_two
    
    if ask_question('+', card_one, card_two, correct):
        print(f"Correct! {card_one} + {card_two} = {correct}")
        keep_track(True)
    else:
        print(f"Wrong! {card_one} + {card_two} = {correct}")
        keep_track(False)
    
    play_again()

def subtract_flashcards():
    system("clear")
    card_one, card_two = random.randint(0, 10), random.randint(0, 10)
    correct = card_one - card_two

    if ask_question('-', card_one, card_two, correct):
        print(f"Correct! {card_one} - {card_two} = {correct}")
        keep_track(True)
    else:
        print(f"Wrong! {card_one} - {card_two} = {correct}")
        keep_track(False)

    play_again()

def multiply_flashcards():
    system("clear")
    card_one, card_two = random.randint(0, 10), random.randint(0, 10)
    correct = card_one * card_two

    if ask_question('*', card_one, card_two, correct):
        print(f"Correct! {card_one} * {card_two} = {correct}")
        keep_track(True)
    else:
        print(f"Wrong! {card_one} * {card_two} = {correct}")
        keep_track(False)

    play_again()

def divide_flashcards():
    system("clear")
    card_one, card_two = random.randint(1, 10), random.randint(1, 10)  # Avoid division by zero
    correct = card_one / card_two

    if ask_question('/', card_one, card_two, correct):
        print(f"Correct! {card_one} / {card_two} = {correct:.2f}")
        keep_track(True)
    else:
        print(f"Wrong! {card_one} / {card_two} = {correct:.2f}")
        keep_track(False)

    play_again()

def fraction_flashcards():
    system("clear")
    card_one = Fraction(random.randint(1, 10), random.randint(1, 10))
    card_two = Fraction(random.randint(1, 10), random.randint(1, 10))
    correct = card_one + card_two

    try:
        user_answer = Fraction(input(f"{card_one} + {card_two} = "))
    except ValueError:
        print("Invalid input! Please enter a fraction in the form 'numerator/denominator'.")
        fraction_flashcards()
        return

    if user_answer == correct:
        print(f"Correct! {card_one} + {card_two} = {user_answer}")
        keep_track(True)
    else:
        print(f"Wrong! {card_one} + {card_two} = {correct}")
        keep_track(False)

    play_again()

def play_again():
    play = input("Would you like another card? yes|no|restart: ").lower()
    if play == "yes":
        if 'flashcard_function' in globals():
            flashcard_function()
    elif play == "no":
        print("Thank you for playing!")
    elif play == "restart":
        start_game()
    else:
        print(f"Sorry, I don't recognize {play}")
        input("Please hit enter to try again.")
        play_again()

def keep_track(correct):
    global global_user_right, global_user_wrong
    if correct:
        global_user_right += 1
    else:
        global_user_wrong += 1

start_game()