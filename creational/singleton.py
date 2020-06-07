#author: vysakh

#what is that?
#Global variable in object oriented way

#why?
#common information (object) shared by multiple objects

#Borg design pattern

class Borg:

	"""Borg class making an class attribute global"""

	_shared_state = {}  #atribute dictionary

	def __init__(self):
		self.__dict__ = self._shared_state

class Singleton(Borg):
	
	"""This class shares all its attributes among its various instances"""

	def __init__(self, **kwargs):
		Borg.__init__(self)
		self._shared_state.update(kwargs)

	def __str__(self):

		return  str(self._shared_state)


x = Singleton(HTTP = 'Hyper Text Transfer Protocol')

print(x)

y = Singleton(SNMP = 'Simple Network Management Protocol')

print(y)				

