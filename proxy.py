#author: vysakh

# used when object is expense to produce
# a proxy class handle object creation
# produce object if only resource available

import time

class Producer:

	"""Define resouce intensive object to instantiate"""

	def produce(self):
		print("Producer is working hard")

	def meet(self):
		print("Producer has time to meet you now")

class Proxy:
	
	"""Define relatively less resouce intensive proxy to instantiate as a middleman"""

	def __init__(self):
		self.occupied = 'No'
		self.producer = None

	def produce(self):

		print("Checking producer is available")

		if self.occupied == 'No':
			self.producer = Producer()
			time.sleep(2)
			self.producer.meet()
		else:
			time.sleep(2)
			print("Producer is not available")



p = Proxy()

p.produce()

p.occupied = 'Yes'

p.produce()
