#author: vysakh

# Adapter converts interface of a class into another one client is expecting

class Korean:

	def __init__(self):
		self.name = 'Korean'

	def speak_korean(self):
		return "An-neyong"

class British:

	def __init__(self):
		self.name = 'British'

	def speak_britsih(self):
		return 'Hello'


class Adapter:
	"""This change generic method names to individualised method names"""
	def __init__(self, object, **adpated_method):
		self._object = object
		self.__dict__.update(adpated_method)

	def __getattr__(self, attr):
		return getattr(self._object, attr)

objects = []

korean = Korean()

british = British()

objects.append(Adapter(korean, speak=korean.speak_korean))
objects.append(Adapter(british, speak=british.speak_britsih))

for obj in objects:
	print("{} says {}".format(obj.name, obj.speak()))	
