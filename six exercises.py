'''
Try FIZZ/BUZZ again but do it in less lines of code!
'''
for number in range (1,101):
	print(f"{number} FizzBuzz!" if number % 3 == 0 and number % 5 == 0 else
          f"{number} Fizz" if number % 3 == 0 else
          f"{number} Buzz" if number % 5 == 0 else
          number)


for number in range(1, 101):
    print(f"{number} FizzBuzz!" if number % 15 == 0 else
          "Fizz" if number % 3 == 0 else
          "Buzz" if number % 5 == 0 else
          number)

'''
Create a multi‐dimensional List with 4 items, and each item is
itself a List containing a personʹs name, their address, and phone
number (make up the info). Loop through the List and output just
each personʹs phone number.
'''
item_1 = ["tim","123 address", "818123456"]
item_2 = ["John","321 address", "818654321"]
item_3 = ["isi","456 address", "818789012"]
item_4 = ["eran","654 address", "818210987"]
multi_list = [item_1, item_2, item_3, item_4]
counter = 0
for num in multi_list:
	print(multi_list[counter][2])
	counter += 1
'''
Loop through the List from exercise 2 and print out the full
information of even items in the List (ie the 2nd and 4th List in your
multidimensional List).
'''
item_1 = ["tim","123 address", "818123456"]
item_2 = ["John","321 address", "818654321"]
item_3 = ["isi","456 address", "818789012"]
item_4 = ["eran","654 address", "818210987"]
multi_list = [item_1, item_2, item_3, item_4]
count = 1
for num in multi_list:
	if count % 2 == 0:
		print(f"Printing even items! {num}")
	else:
		pass #Skip odd numbers	
	count += 1
	