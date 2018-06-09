#author: vysakh

#used to clone or copy objects rather than creating expensive objects

import copy

class Prototype():

	def __init__(self):
		self._objects = {}

	def register_objects(self, name, obj):
		"""Register an objects"""

		self._objects[name] = obj

	def unregister_objects(self, name):
		"""Unregister an object"""
		del self._objects[name]

	def clone(self, name, **args):
		"""clone object"""

		obj = copy.deepcopy(self._objects.get(name))
		obj.__dict__.update(args)
		return obj



class Car():

	def __init__(self):

		self.model = "BMW"
		self.color = 'Red'
		self.options = 'Ex'

	def __str__(self):

		return "{}|{}|{}".format(self.model,self.color,self.options)


c = Car()

print(c)

prototype = Prototype()

prototype.register_objects('clone_car',c)

c1 = prototype.clone('clone_car')

print(c1)	