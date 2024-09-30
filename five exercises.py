'''
Create a List with the names of five people you know and output
the second name to the screen.
'''
names = ["mark", "tal", "eran", "isi", "udi"]
print(names[1])

'''
Create a List where the first item in the List is a math problem,
like 1 + 1 and the rest of the items are names. Output the first item
to the screen. (WOAH, MATH can be an item in a List?!)
'''
comb_list = [1+1,"mark", "tal", "eran", "isi", "udi"]
print(comb_list[0])

'''
Create a multi‐dimensional List with 4 items, and each item is
itself a List containing a personʹs name, their address, and phone
number (make up the info). Output the second item in your
multidimensional List.
'''
item_1 = ["mark", "123 address ","818223344"]
item_2 = ["john", "321 address ","818123456"]
item_3 = ["isi", "456 address ","818654321"]
item_4 = ["eran", "654 address ","818789012"]
multi_list = [item_1, item_2, item_3, item_4]
print(multi_list[1])

'''
Output just the phone number of the third item in your List from
the last question.
'''
item_1 = ["mark", "123 address ","818223344"]
item_2 = ["john", "321 address ","818123456"]
item_3 = ["isi", "456 address ","818654321"]
item_4 = ["eran", "654 address ","818789012"]
multi_list = [item_1, item_2, item_3, item_4]
print(multi_list[2][2])

