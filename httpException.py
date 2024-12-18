
class HttpException(Exception):
	statusCode = None
	message = None
	def __init__(self):
		super().__init__(f'Status Code: {self.statusCode} and message is: {self.message}')

class NotFound(HttpException):
	statusCode=404
	message = 'Resource not found'

class ServerError(HttpException):
	statusCode = 500
	message = 'The Server messed up!'

def raiseServerError():
	print(ServerError())

raiseServerError()