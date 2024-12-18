
# Handiling Exceptions / Custom exception

import time

# Try/Except 
def causeError():
	try:
		return 1/0
	except Exception as e:
		return e

def causeErrorPrint():
	try:
		return 1/0
	except Exception:
		print ('There was some sort of error!')

# using finally will always execute if there is an error or not 
# and can be used with or without try/except 
# finally can be used as a cleaneup / loggin / printup after a statment complete
# no matter what happens inside the try block
def causeErrorFinally():
	start = time.time()
	try:
		time.sleep(0.5) # pause for half a second 
		return 1/0
	except Exception:
		print ('There was some sort of error!')
	finally:
		print(f'function took {time.time() - start} seconds to execute')

def callCauseError():
	return causeError()


def callCauseErrorException():
	try:
		return 1/0
	except TypeError:
		print('There was a type error!')
	except ZeroDivisionError:
		print('There was a zero division error!')
	except Exception:
		print ('There was some sort of error!')

# Custom Decorators
def handleException(func):
	def wrapper(*args):
		try:
			func(*args)
		except TypeError:
			print('There was a type error!')
		except ZeroDivisionError:
			print('There was a zero division error!')
		except Exception:
			print ('There was some sort of error!')
	return wrapper

@handleException
def causeErrorHandleException():
	return 1/0

@handleException
def raiseError(n):
	if n == 0:
		raise Exception()
	print(n)

# Custom Exceptions
class CustomException(Exception):
	pass

def causeCustomException():
	raise CustomException() 



e = callCauseError()
print(type(e))
causeErrorPrint()
causeErrorFinally()
callCauseErrorException()
causeErrorHandleException()
raiseError(0)
causeCustomException('You called the causeCustomException function!')