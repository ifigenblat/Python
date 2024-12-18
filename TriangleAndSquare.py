
'''
write a function called square that returns the square of a number using only the triangle function. 
No multiplication or exponents allowed!

Hint: sum of 2 not identical triangles equal a square
'''
def triangle(num):
    if num == 1:
        return num
    return num + triangle(num - 1)

def square(num):
    if num == 1:
        return num
    sums = triangle(num)
    sums = sums + triangle(num - 1)
    return sums

print(square(5))
print(square(6))