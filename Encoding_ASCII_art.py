'''
Encoding ASCII art

A String like 'AAAAABBBBAAA' can be efficiently represented 
as "5 a's followed by 4 b's followed by 3 a's'"

Write function encodString that will encode a string like 'AAAAABBBBAAA'
and return a list of tuples: [(A:5),(B:4),(A:3)]

then add a corresponding function decodeString that will taje in a list of tuples and
print the original string.
'''


def encodeString(stringVal):
    counter = 0
    temp = ''
    my_list = []
    num = 1
    for char in stringVal:
        if(num < len(stringVal)):
            if temp == '':
                temp = char
                counter = counter + 1
            elif temp == char:
                counter = counter + 1
            else:
                my_tuples = (temp,counter)
                my_list.append(my_tuples)
                temp = char
                counter = 1
            num = num + 1
        else:
            counter = counter + 1
            my_tuples = (temp,counter)
            my_list.append(my_tuples)    
    return my_list
    pass

def decodeString(encodedList):
    stringDecod = ''
    for key, value in encodedList:
        counter = 0
        number = value
        while counter < number:
            stringDecod = stringDecod + key
            counter = counter + 1
    return stringDecod
    pass

list = encodeString('AAAAABBBBAAA')
print(list)
decoded = decodeString(list)
print(decoded)