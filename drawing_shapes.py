'''
Inheriate the shape class into square and triangle and print to the screen 
'''

class Shape:
	width = 5
	height = 5
	printChar = '#'

	def printRow(self, i):
		raise NotImplementedError("Will be implemented by children extending this class")

	def print(self):
		for i in range(self.height):
			self.printRow(i)


class Square(Shape):
	def printRow(self, i):
		print(self.printChar * self.width)

class Triangle(Shape):
	def printRow(self, i):
		print(self.printChar * (i + 1))


class EquilateralTriangle(Shape):
	height = 5
	width = 2 * height

	def printRow(self, i):
		triangleWidth = i * 2 + 1
		padding = int((self.width - triangleWidth)/2)
		print(' '*padding + self.printChar * triangleWidth)



square = Square()
square.print()

triangle = Triangle()
triangle.print()

equilateraltriangle = EquilateralTriangle()
equilateraltriangle.print()