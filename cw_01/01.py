#coding: utf-8

class Car(object):

	km = 0

	def __init__(self, model='t'):
		self.speed = 60
		self.model = model

	def run(self, time=1):
		self.km += self.speed * time
		print(self.model, 'was moved ', self.km, ' km')

class Truck(Car):

	def __init__(self, speed=40, model='t'):
		self.speed = 40	
		self.model = model
	pass

class Hellicopter(Car):

	def __init__(self, model='t'):
		self.speed = 260
		self.model = model
	pass


transport = [ Truck(speed=60, model='Maz'), Truck(60), Car(), Hellicopter() ]

for t in transport:
	t.run(10)

for t in transport:
	t.run(10)