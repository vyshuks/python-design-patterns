#author: vysakh

# for using creation of complex objects
# Have 4 parts
#1. Director
#2. Abstract Class
#3. Concrete Class
#4. Product

class Director():
	"""Director Class"""

	def __init__(self, builder):
		self._builder = builder

	def create_car(self):
		self._builder.create_new_car()
		self._builder.add_model()
		self._builder.add_tire()
		self._builder.add_engine()

	def get_car(self):
		return self._builder.car


class Builder():
	"""Abstract Class"""

	def __init__(self):
		self.car = None

	def create_new_car(self):
		self.car = Car()


class FordBuilder(Builder):
	"""Concrete Class"""

	def add_model(self):
		self.car.model = "Ford"

	def add_tire(self):
		self.car.tire = "F tires"

	def add_engine(self):
		self.car.engine = 'F engine'

class Car():
	"""Product Class"""

	def __init__(self):
		self.model = None
		self.tire = None
		self.engine = None

	def __str__(self):
		return "{}|{}|{}".format(self.model,self.tire,self.engine)		




ford = FordBuilder()
director = Director(ford)

director.create_car()
car = director.get_car()

print(car)