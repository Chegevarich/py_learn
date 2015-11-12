# coding: utf-8
from abc import ABCMeta, abstractmethod
from time import sleep

class SuperBody(metaclass=ABCMeta):

	#чтение из некоторого источника данных
	#в целом для переопределения и замены 
	#на свой источник 
	#TODO описать формат треуемых данных
	@abstractmethod
	def read_data(self):
		return open(self.source)

	#сбор всех координат в единую переменную 
	#координаты стоит вернуть следующим форматом
	#dict time => [lng, lnt]
	@abstractmethod
	def take_all_coords_by_event(self, event):
		coords_by_event = self.read_data()
		for i in coords_by_event:
			dict_coords{'time':[lnt, lng]}

		return dict_coords

	#создание объекта 
	#event - событие, вероятно описанное в БД 
	#как временной промежуток
	#к event привязаны координаты через хранимую процедуру
	#
	#timestep - шаг вывода данных - раз в timestep минут
	#вероятно стоит дополнить источником данных 
	#возможно классом для чтения данны либо либо
	@abstractmethod
	def __init__(self, event, timestep, source):
		self.time = timestep
		self.coords = self.take_all_coords_by_event(self, event)
		self.source = source
	#возвращение по из общего пулла координат
	#набор координат за держкой по времени 
	#координаты привязаны к времени time
	@abstractmethod
	def coords(self, time):
		sleep(self.time)
		return self.coords[time]

	#запуск чтения ?
	@abstractmethod 
	def coordsreader(self):
		for i in self.coords:
			self.coord(i)