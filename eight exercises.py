'''
Create your own Dictionary, with five of your friendsʹ names and
their phone numbers.
'''
friends = {"eran":"12345","tamir":"23456","tim":"34567","tom":"45678","john":"56789"}

print(friends)


'''
Create a program using your answer to exercise 1 that prompts a
user to enter a name from your list your five friends, and then
returns the phone number for that specific friend.
'''
name = input("Please enter a name: ")
for x,y in friends.items():
	if(name == x):
		print (f"The phone number for {x} is {y}")

'''
Add a feature to your code from exercise 2 that allows people to
add or delete a name from the Dictionary, then return the
updated Dictionary to the screen.
'''
answer = input("Please write Delete or Add if you like to delete or add item to the dictionary: ")
if(answer == "Add"):
	name = input("What is your friend name? ")
	phone = input("What is your friend phone number? ")
	friends [name] = phone
elif(answer == "Delete"):
	name = input("Which friend would you like to delete? ")
	for x,y in friends.items():
		if(x == name):
			friends.pop(name)
			break

print(f"Your list now is: {friends}")

'''
Create a loop that cycles through your Dictionary from exercise 1
and outputs (one per line) ʺMy friend Xʹs phone number is: xxx‐
xxx‐xxxxʺ  replacing the xʹs with the persons actual name and
phone number.
'''

for x,y in friends.items():
	print(f"My friend {x}'s phone number is: {y}")