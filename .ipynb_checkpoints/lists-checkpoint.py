'''
LISTS START WITH ZERO!
'''
names = ["John", "Tim", "Mary", "Beatrice", "Bluto"]
print(names[2])
print(names)

variable_1 = "Tim"
names = ["John", variable_1, "Mary", 41, "Bluto"]
print(names[1])

names = []

names = ["John", "April"]
print(len(names))

# only append ONE item, to the end.
names = ["John", "April"]
names.append("Bob")
print(names)

names = ["John", "April"]
names.insert(0,"Bob")
print(names)

# Cam add multiple items to the list
names = ["John", "April"]
names.extend(["Tim", "Bob"])
print(names)

# will only remove the first one incase there are more then one Bluto
names = ["John", "Tim", "Mary", "Beatrice", "Bluto"]
names.remove("Bluto")
print(names)

names = ["John", "Tim", "Mary", "Beatrice", "Bluto"]
names.pop(0)
print(names)

names = ["John", "Tim", "Mary", "Beatrice", "Bluto"]
names.pop(1)
print(names)

names = ["John", "Mary", "Beatrice", "Bluto", [1,2,3,4]] 
print(names)

# Accessing nested list within our list; List location 4 priting second item.
names = ["John", "Mary", "Beatrice", "Bluto", [1,2,3,4]] 
print(names[4][2])

# Multidimensional lists
numbers = [1,2,3,4]
names = ["John", "Mary", "Beatrice", "Bluto", numbers]
print(names[4][2]) 