'''
Finding prime number using For/Else
for number in range(2,100):
	for factor in range(2, int(number **0.5)+1):
		if number % factor == 0:
			break
	else:
		print(f'{number} is prime!')
'''

for number in range(2,100):
	# Go through all number from 2 to 100
	for factor in range (2, int(number **0.5)+1):
		'''
		range(2, int(number ** 0.5) + 1):
			* Start at 2 (smallest possible factor for most numbers).
			* Go up to the integer value of the square root of the number plus 1.
				* Adding 1 ensures the square root itself is included if it’s an integer.
		for factor in range(...):
			* Loops through each number in the range (2 to the square root).
		'''
		if number % factor == 0:
			break
	else:
		print(f'{number} is prime!')


# Write a function called allPrimesUpTo which returns a list of all prime numbers up to given number.

def allPrimesUpTo(num):
    my_list=[]
    for number in range(2,num):
        for factor in range(2, int(number**0.5)+1):
            if number % factor == 0:
                break
        else:
             my_list.append(number)
    return my_list


# write the function more efficiently

def allPrimesUpTo2(num):
    my_list=[2]
    for number in range(3,num):
    	squarerootNum = number**0.5
    	for factor in my_list:
            if number % factor == 0:
            	#Not Prime
                break
            if factor > squarerootNum:
            	# It's Prime!
            	my_list.append(number)
            	break
    return my_list


print(allPrimesUpTo(100))
print(allPrimesUpTo2(100))