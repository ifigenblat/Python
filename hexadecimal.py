# Python code below
hexNumbers = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
}

# Converts a string hexadecimal number into an integer decimal
# If hexNum is not a valid hexadecimal number, returns None
def hexToDec(hexNum):
    if len(hexNum) > 3:
        return None
    for char in hexNum:
        if char.lower() > 'f':
            return None
    temp = 0
    slicing = hexNum[::-1].upper()
    for i in range (len(hexNum)):
        char = hexNumbers[slicing[i]]
        if i == 0:
            temp = char * 1
        if i == 1:
            temp = temp + char * 16
        if i == 2:
            temp = temp + char * 256
    return temp


#Another solution:
def hexToDec2(hexNum):
    for char in hexNum:
        if char.upper() not in hexNumbers:
            return None
    
    if len(hexNum) == 3:
        return hexNumbers[hexNum[0].upper()] * 256 + hexNumbers[hexNum[1].upper()] * 16 + hexNumbers[hexNum[2].upper()]

    if len(hexNum) == 2:
        return hexNumbers[hexNum[0].upper()] * 16 + hexNumbers[hexNum[1].upper()]

    if len(hexNum) == 1:
        return hexNumbers[hexNum[0].upper()]



hexnum = input("please provide an up to 3 character string to convert from hexadecimal to decimal: ")
result = hexToDec2(hexnum)
print(f"{result}")