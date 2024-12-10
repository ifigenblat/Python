# While loops

'''
while  conditional:
   do something
'''

num = 0
while num < 10:
	print(num)
	num += 1

'''
while  conditional
   do something
  if conditional
break
'''
num = 0
while num < 10:
	num += 1
	if num == 5:
		break
	print(num)

num = 0
while num < 10:
	num += 1
	if num == 5:
		continue
	print(num)

# FOR LOOPS
'''
num automaticlly set to 0 by the for loop
number in ranges, like Lists, start at zero
'''
for num in range(6):
	print(num)

'''
specify a starting point if you donʹt want to start at 0
'''
for num in range(1,6):
	print(num)

for num in range(6):
	print("I love Cheese! ")

# Looping through a list
names = ["john", "mary", "tim"]
for name in names:
	print(name)

myList = [1,2,3,4]
for item in myList:
	print(item)

# iteriate through carcters 
name = "John Smith"
for x in name:
	print(x)

# Using elif with for
for x in range(3):
	print(x)
else:
	print("ALL DONE")

# Pass Statement - for loop can't be empty
for x in range(3):
	pass

'''
Example:
Suppose you're iterating over a list of numbers, 
and you want to skip the even numbers
but haven't decided what to do with the odd numbers yet. 
You can use pass like this:
'''
numbers = [1, 2, 3, 4, 5]

for number in numbers:
    if number % 2 == 0:
        pass  # Skip even numbers
    else:
        print(f"Odd number: {number}")


'''
Finding prime number using For/Else
'''
for number in range(2,100):
	for factor in range(2, int(number **0.5)+1):
		if number % factor == 0:
			break
	else:
		print(f'{number} is prime!')