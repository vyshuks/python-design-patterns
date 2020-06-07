#author: vysakh

class Dog:
	"""One of the object to be returned"""

	def speak(self):
		return "Woof"

	def __str__(self):
		return "Dog"

class DogFactory:
	"""Concrete Factory"""		

	def get_pet(self ):
		"""Return Dog object"""
		return Dog()

	def get_food(self):
		"""Return dog food object """
		return "Dog food!"


class PetStore:
	
	"""PetStore houses our abstract factory"""

	def __init__(self, pet_factory = None):
		self._pet_factory = pet_factory	

	def show_pet(self):
		"""Utility method used to display deatils of object return by the factory"""
		pet = self._pet_factory.get_pet()
		pet_food = self._pet_factory.get_food()

		print("Our pet {}".format(pet))
		print("Our pet speak {}".format(pet.speak()))
		print("Our pet food is {}".format(pet_food))	


factory = DogFactory()

shop = PetStore(factory)

shop.show_pet()
