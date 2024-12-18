# Defining CLass

class Dog:
	def __init__(self, name):
		self.name = name
		self.legs = 4

	def speak(self):
		print(self.name + ' says: Bark!')


my_dog = Dog('Rover')
another_dog = Dog('Fluffy')

my_dog.speak()
another_dog.speak()

# Inheritance
class Chihuahua(Dog):
	def speak(self):
		print(f'{self.name} says: Yap yap yap')

	def wagTail(self):
		print('Vigorous wagging')

		
dog = Chihuahua('Roxy')
dog.speak()
dog.wagTail()


# Inheritance with python built in classes 
class UniqueList(list):
 	# Overwrite the append function
 	def append(self, item):
 		if item in self:
 			return
 		super().append(item)

uniqueList = UniqueList ()
uniqueList.append(1)
uniqueList.append(1)
uniqueList.append(2)

print(uniqueList)

# Inheritance with constructor 
class UniqueList(list):
	def __init__(self):
		super().__init__()
		self.someProperty = 'Unique List!'
	
	# Overwrite the append function
	def append(self, item):
		if item in self:
			return
		super().append(item)

uniqueList = UniqueList ()
uniqueList.append(1)
uniqueList.append(1)
uniqueList.append(2)

print(uniqueList.someProperty)

class WordSet:
	def __init__(self):
		self.words = set()

	def addText(self, text):
		text = self.cleanText(text)
		for word in text.split():
			self.words.add(word)

	def cleanText(self, text):
		#chaining functions 
		text = text.replace('!', '').replace('.', '').replace(',', '').replace('\'', '')
		return text.lower()


wordSet = WordSet()
wordSet.addText('Hi, I\'m Ryan! Here is a sebtence I want to add!')
wordSet.addText('Here is another sentence I want to add.')

print(wordSet.words)