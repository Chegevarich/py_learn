# coding:utf-8
# python v3+
from abc import ABCMeta, abstractmethod

class SuperFarm(metaclass=ABCMeta):

	@abstractmethod
	def __init__(self, ducks, dogs, cows ):
		animals = { 'ducks':[], 'dogs':[], 'cows':[] }
		for i in range(10):
			animals[0].append(Cow())
		for i in range(10):
			animals[1].append(Dog())
		for i in range(10):
			animals[2].append(Duck())

	@abstractmethod
	def append_animal(self, animal_type, animal_properties):
		self.animals[animal_type].append(Animal(animal_properties))

	@abstractmethod
	def next_month(self, month, day_in_month):
		for animal in self.animals:
			animal.do_somefing()

	@abstractmethod
	def report(self):
		print(self.total_info)