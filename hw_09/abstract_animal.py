# coding:utf-8
# python v3+
from abc import ABCMeta, abstractmethod

class SuperAnimal(metaclass=ABCMeta):

	@abstractmethod
	def __init__(self, main_product, main_product_coefficent, main_product_unit, speed, travel_time_per_day):
		self.option = values

	@abstractmethod
	def make_animal_affairs(self, month=1):
		self.run(month*30)
		self.voice(month*30)
		self.goods(month)
		self.total_moth_in_own +=month

	@abstractmethod
	def run(self, days):
		self.distance_traveled += self.distance_traveled_in_last_moth

	@abstractmethod
	def voice(self, days):
		self.voice_used += self.voice_in_last_moth

	@abstractmethod
	def goods(self, month):
		self.goods_ready += self.goods_in_last_month