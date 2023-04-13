class Pets: #super class
	def __init__(self, pType, name, birthdate, breed, color):
		self.__type = pType
		self.__name = name
		self.__birthdate = birthdate
		self.__breed = breed
		self.__color = color

	#GETTERS AND SETTERS for each parameter

	def getName(self):
		return self.__name
	def setName(self, pName):
		self.__name = pName

	def getBirthdate(self):
		return self.__birthdate
	def setBirthdate(self, birthdate):
		self.__birthdate = pBirthdate

	def getBreed(self):
		return self.__breed
	def setBreed(self, pBreed):
		self.__breed = pBreed

	def getType(self):
		return self.__type
	def setType(self, pType):
		self.__type = pType

	def getColor(self):
		return self.__color
	def setColor(self, pColor):
		self.__color = pColor
#	def introduce(self): #instance method
#		return "My name is " + self.__firstName + " " + self.lastName

	def __str__(self):
		strOutput = ("Name: " + self.__name + " Birthdate: " + self.__birthdate + " Breed: " + self.__breed + " Type: " + self.__type + " Color: " + self.__color)
		return strOutput

class Dog(Pets):#sub class 1
	def __init__(self, name, birthdate, breed, color):
		Person.__init__(self, pName, pBirthdate, pBreed, pColor)

		#strOutput = ("First Name: " + self.firstName + " / Last Name: " + self.lastName + "Major: " + self.major + " / School: " + self.school)
	def __str__(self):
		strOutput = ("Name: " + self.name + " Birthdate: " + self.birthdate + " Breed: " + self.breed + " Color: " + self.color)
		return strOutput

class Cat(Pets):#sub class 2
	def __init__(self, name, birthdate, breed, color):
		Person.__init__(self, pName, pBirthdate, pBreed, pColor)
	def __str__(self):
		strOutput = ("Name: " + self.name + " Birthdate: " + self.birthdate + " Breed: " + self.breed + " Color: " + self.color)
		return strOutput

class Fish(Pets):#sub class 3
	def __init__(self, name, birthdate, breed, color):
		Person.__init__(self, pName, pBirthdate, pBreed, pColor)
		self.pBreed = pType
	def __str__(self):
		strOutput = ("Name: " + self.name + " Birthdate: " + self.birthdate + " Type: " + self.pType + " Color: " + self.color)
		return strOutput

class Bird(Pets):#sub class 4
	def __init__(self, name, birthdate, breed, color):
		Person.__init__(self, pName, pBirthdate, pBreed, pColor)
		self.pBreed = pType
	def __str__(self):
		strOutput = ("Name: " + self.name + " Birthdate: " + self.birthdate + " Type: " + self.pType + " Color: " + self.color)
		return strOutput
