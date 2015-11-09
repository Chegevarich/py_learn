# coding: utf-8
from abc import ABCMeta, abstractmethod

class SuperBody(metaclass=ABCMeta):

	@abstractmethod
	def take_all_coords_by_event(self, event):
		coords_by_event = []
		return coords_by_event

	@abstractmethod
	def __init__(self, event):
		self.coords = self.take_all_coords_by_event(self, event)

	@abstractmethod
	def coords(self, time):
		return self.coords[time]