# coding: utf-8
from abc import ABCMeta, abstractmethod
from time import sleep
from supercoordreader import SuperBody
import os, sys
import xml.etree.ElementTree as ET

class DataProvider():

	#чтение из некоторого источника данных
	#в целом для переопределения и замены 
	#на свой источник 
	#TODO описать формат треуемых данных
	
	def read_data(self):
		return open(self.source)


	def read_data_from_xml(self):
		self.xml = ET.fromstring(str(open(self.source).read()))

	def take_all_coords_by_event_from_xml(self):
		events = self.xml.findall('event')
		for e in events:
			if e.get('code') == self.event:
				event = e
		if e:
			self.event_data = e
		else:
			return False

	def coords_to_dict_from_xml(self):
		for e in self.event_data:
			for i in e.iter('coord'):
				print(i.get('lng'),i.get('lnt'), i.get('time'))
	#сбор всех координат в единую переменную 
	#координаты стоит вернуть следующим форматом
	#dict time => [lng, lnt]
	def take_all_coords_by_event(self, event):
		coords_by_event = self.read_data()
		for i in coords_by_event:
			dict_coords.append['time'] = [lnt, lng]

		return dict_coords

	#создание объекта 
	#event - событие, вероятно описанное в БД 
	#как временной промежуток
	#к event привязаны координаты через хранимую процедуру
	#
	#timestep - шаг вывода данных - раз в timestep минут
	#вероятно стоит дополнить источником данных 
	#возможно классом для чтения данны либо либо
	
	def __init__(self, event, timestep, source):
		self.time = timestep
		self.event = event
		#self.coords = self.take_all_coords_by_event(self, event)
		self.source = source
	#возвращение по из общего пулла координат
	#набор координат за держкой по времени 
	#координаты привязаны к времени time
	
	def coords(self, time):
		sleep(self.time)
		return self.coords[time]

	#запуск чтения ?
	def coordsreader(self):
		for i in self.coords:
			self.coord(i)

DP = DataProvider('first_sample_event', 1, './sample_data/sample_event0.xml')


#TODO make method
DP.read_data_from_xml()
DP.take_all_coords_by_event_from_xml()
DP.coords_to_dict_from_xml()

#TODO end of make method

#DP.take_all_coords_by_event_from_xml()