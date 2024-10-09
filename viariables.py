'''
Variables are like buckets.  You can put stuff in them and dump stuff out
of them.   
In Python, you create a variable just by naming it and sticking
something in it
Name variables short but descriptive
keep your variable names lowercase
'''
my_name = "John smith"
my_age = 38
print (f"My name is {my_name} and My age is {my_age}")


number_1 = 5
number_2 = 10
print(number_1 + number_2)

'''
plus sign (+) for strings is used to concatenate the two
variables. Whenever weʹre working with strings and we want to add
something in, or concatenate it in, we use the plus sign
'''
fruit_1 = "apples"
fruit_2 = "oranges"
print(fruit_1 + fruit_2) 

fruit_1 = "apples"
fruit_2 = "oranges"
print("I Like " + fruit_1 + " and I like " + fruit_2) 

# or a better way

fruit_1 = "apples"
fruit_2 = "oranges"
print(f"I Like {fruit_1} and I like {fruit_2}") 

fruit_1 = "apples"
print(fruit_1 * 5) 