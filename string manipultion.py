'''
lower()    Convert to all lowercase
upper()    Convert to all uppercase
capitalize()    Capitalize just first letter
title()     Capitalizes first letter of each word  
swapcase()    Switches capitalized to lowercase & vice versa
len()     *Returns character length
rstrip()    Removes trailing spaces
'''

# Realtime comvertion
name = input("What's your name ")
print(f'Hi there {name.lower()}')

# Assign permanently 
name = input("What's your name ")
name = name.lower()
print(f"Hi there {name}")

# Only len() don't slap at the end of the variable 
name = input("What's your name ")
print(f'The name {name} has {len(name)} characters')