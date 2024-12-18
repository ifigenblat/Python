'''
Write a custom annotation that handles bad arguments
Raise a custom exception if any of the arguments passed to the function are not integer
'''

def handleNonIntArguments(func):
    def wrapper(*args):
        non_integers = [arg for arg in args if not isinstance(arg, int)]
        if(non_integers):
            raise NonIntArgumentException('Non Integer Found!')
        return func(*args)
    return wrapper

    # another solution 
    def wrapper(*args):
        for item in args:
            if type(item) is not int:
                raise NonIntArgumentException()
        return func(*args)
    return wrapper

class NonIntArgumentException(Exception):
    pass

@handleNonIntArguments
def sum(a, b, c):
    return a + b + c

try:
    result = sum(1, 2, 'a')
    print('This should not print out')
except NonIntArgumentException as e:
    print('Hooray!')
try:
    result = sum(1.0, 2.0, 3.0)
    print('This should not print out')
except NonIntArgumentException as e:
    print('Hooray!')
try:
    result =  sum(1, 2, 3)
    print(f'Result: {result}')
except NonIntArgumentException as e:
    print('Hooray!')