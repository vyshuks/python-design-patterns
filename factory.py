#author: vysakh

#Factory is an object specialised and creating other objects

#Problem?
#1. when type of object not certain
#2.Decision to be made at runtime regarding what class to  used

class Dog:

	""" A simple Dog class """

	def __init__(self, name):
		self._name = name

	def speak(self):
		return "Woof"

class Cat:

	"""A simple Cat class"""

	def __init__(self, name):
		self._name = name

	def speak(self):
		return "Meow"


def get_pet(pet = "dog"):
	
	"""The factory method"""

	pets = dict( dog = Dog("hope"), cat = Cat("peace"))	
	return pets[pet]

d = get_pet("dog")

print(d.speak())


c = get_pet("cat")

print(c.speak())		

