'''
Print out every number between 1 and 100, one
number per line, but if the number is divisible by three, print out ʺFizzʺ;
if the number is divisible by five, print out ʺBuzzʺ; and if the number is
divisible by both three AND five, print out FIZZ BUZZ.
'''
for number in range (1,101):
	if number % 3 == 0 and number % 5 == 0:
		print (f"{number} FizzBuzz!")
	elif number % 3 == 0:
		print(f"{number} Fizz")
	elif number % 5 == 0:
		print(f"{number} Buzz")
	else:
		print(number)

