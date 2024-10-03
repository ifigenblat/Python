'''
The items in our Dictionary are called ʺKeyʺ and ʺValueʺ pairs
With a Dictionary, the ʺKeyʺ is whatever you want it to be.  In this case,
weʹre using names as Keys. 
'''

favorite_pizza = {
	"John":"Pepperoni", 
	"Tim":"Mushroom",
	"Mary":"Cheese",
	"Beatrice":"Ham and Onion",
	"Bluto":"Supreme"
	}
print(favorite_pizza["John"])

'''
ADDING AND REMOVING ITEMS FROM A DICTIONARY
'''
favorite_pizza = {
	"John":"Pepperoni", 
	"Tim":"Mushroom",
	"Mary":"Cheese",
	"Beatrice":"Ham and Onion",
	"Bluto":"Supreme"
	}

print(f"Before adding Bob {favorite_pizza}")
favorite_pizza["Bob"] = "Tuna"
print(f"After adding Bob {favorite_pizza}")

favorite_pizza = {
	"John":"Pepperoni", 
	"Tim":"Mushroom",
	"Mary":"Cheese",
	"Beatrice":"Ham and Onion",
	"Bluto":"Supreme"
	}

favorite_pizza.pop("Tim")
print(f"After poping out Tim {favorite_pizza}")

'''
DICTIONARY ODDS AND ENDS
If you want to access that item of the Dictionary,
you can do it two different ways, either by calling it by the variable
name (user_name), or the actual value that we assigned to that variable
(John)
'''
user_name = "John"
favorite_pizza = {
	user_name:"Pepperoni", 
	"Tim":"Mushroom",
	"Mary":"Cheese",
	"Beatrice":"Ham and Onion",
	"Bluto":"Supreme"
	}
print(favorite_pizza)

'''
you could call it like this:
	print(favorite_pizza[user_name])
or you could also call it like this:
	print(favorite_pizza[ʺJohnʺ])
'''
'''
Blutoʹs favorite pizza has been changed to 41,
which is a number.  You can do numbery things to it now.
'''
favorite_pizza = {"John":"Pepperoni",  "Tim":"Mushroom",  "Mary":"Cheese",
"Beatrice":"Ham and Onion", "Bluto":41}

print(favorite_pizza["Bluto"]+3)

'''
FINDING THE KEYS OR VALUES OF A DICTIONARY
'''
favorite_pizza = {
	"John":"Pepperoni", 
	"Tim":"Mushroom",
	"Mary":"Cheese",
	"Beatrice":"Ham and Onion",
	"Bluto":"Supreme"
	}

print(favorite_pizza.keys())

print(favorite_pizza.values())

'''
LOOPING DICTIONARIES TO GET KEYS AND VALUES
'''
favorite_pizza = {
	"John":"Pepperoni", 
	"Tim":"Mushroom",
	"Mary":"Cheese",
	"Beatrice":"Ham and Onion",
	"Bluto":"Supreme"
	}

for x,y in favorite_pizza.items():
	print(f"Key:{x} Value:{y}") 

print(f"Printing favorite_pizza.items: {favorite_pizza.items()}")