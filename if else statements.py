'''
IF
if conditional:
   do something here
'''
x = 41
if x == 41:
	print("X does in fact equal to 41!")

'''
IF/ElSE
if conditional:
     do something here
else:
   do something else
'''
x = 41
if x == 42:
	print("X does in fact equal to 41!")
else:
	print("X does Not equal to 41!")

'''
IF/ELIF
if conditional:
     do something here
elif conditional:
     do something here
else:
   do something else
'''
name = "John"
if name == "Bob":
	print(" Hi there Bob!")
elif name == "John":
	print("What up John!!")
else:
	print(" I don't know who you are!")

'''
AND OR
'''
name = "John"
if name == "Bob" or name == "John":
	print("Hi there John or Bob!")


name = input("Enter your name ")
if name == "Bob" or name == "John":
	print(f"Hi there {name}!")
else:
	print("Hi there stranger!")