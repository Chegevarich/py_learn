# coding: utf-8
from abc import ABCMeta, abstractmethod
from time import sleep, time
from datetime import datetime
from supercoordreader import SuperBody
import os, sys
import xml.etree.ElementTree as ET

class DataProvider(SuperBody):

	#чтение из некоторого источника данных
	#в целом для переопределения и замены 
	#на свой источник 
	#TODO описать формат треуемых данных
	
	def read_data(self):
		return open(self.source)


	def read_data_from_xml(self):
		self.xml = ET.fromstring(str(open(self.source).read()))

	def take_all_coords_by_event_from_xml(self):
		#все эвенты из подгруженного файла
		events = self.xml.findall('event')

		#ищем в эвентах эвент с нужным кодом
		for e in events:
			#если код совпадает с искомым евентом
			if e.get('code') == self.event:
				event = e

		#если получили эвент - запоминаем эвент
		if e:
			self.event_data = e
		else:
			return False

	def coords_to_dict_from_xml(self):

		#перебираем юниты
		for u in self.event_data:
			#
			for c in u.iter('coord'):
				#print(u.tag)

				if u.get('unit_code') not in self.coord_array:
					self.coord_array[u.get('unit_code')] = []

				self.coord_array[u.get('unit_code')].append(  [c.get('lng'), c.get('lnt'), c.get('time')]  )
				
		for i in self.coord_array:
			self.coord_array[i].sort(key=lambda x: x[2])
			#print(self.coord_array[i])


	def make_start_time(self):
		self.start_time = int(time())
		self.end_time = int(0)	

		#перебираем каждый юнит
		for u in self.coord_array:
			#у каждого юнита рассматриваем геоданные
			for i in self.coord_array[u]:
				if self.end_time < int(i[2]):
					self.end_time = int(i[2])

				if self.start_time > int(i[2]):
					self.start_time = int(i[2])
			

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
		self.coord_array = {}
		self.coords_by_time_dict = {}

		self.time = timestep
		self.event = event
		#self.coords = self.take_all_coords_by_event(self, event)
		self.source = source
		self.current_tume = 0
		

	#возвращение по из общего пулла координат
	#набор координат за держкой по времени 
	#координаты привязаны к времени time
	def coords(self, time):
		#sleep(self.time)

		for u in self.coord_array:
			#у каждого юнита рассматриваем геоданные
			for i in self.coord_array[u]:
				if int(self.start_time) > int(i[2]):
					self.start_time = int(i[2])

		self.current_tume +=1

		return self.coords[time]

	#формируем список для наблюдения в разрезе времени 
	def coords_by_time(self):

		#each key as unit name
		for u in self.coord_array:
			#each list coords bu unit 
			for i in self.coord_array[u]:
				#if current dict has no element for this second - create it
				if i[2] not in self.coords_by_time_dict:
					self.coords_by_time_dict[i[2]] = []
				#add new coord by unit of current second
				self.coords_by_time_dict[i[2]].append([u, i])
					

	#запуск чтения ?
	def coordsreader(self):
		for i in self.coords:
			self.coord(i)

	def test(self):
		print(self.coords_by_time_dict)

	def retrospective_read(self):
		
		print(self.coords_by_time_dict.keys())

		for i in range(self.start_time, self.end_time):
			#print( i )

			if str(i) in self.coords_by_time_dict.keys():
				print(self.coords_by_time_dict[str(i)])
				pass
			else:
				pass
				#print('nofing new')
			sleep(1)
		#print(self.start_time, self.end_time)



if __name__ == '__main__':

	DP = DataProvider('first_sample_event', 1, './sample_data/sample_event0.xml')

	#TODO make method -> xml_init
	#load xml from file
	DP.read_data_from_xml()
	#parse typical xml
	DP.take_all_coords_by_event_from_xml()
	#make dict [unit] => [ [lnt, lng, time], [ lnt, lng, time] ]
	DP.coords_to_dict_from_xml()
	#time from 
	DP.make_start_time()
	#reader by time
	DP.coords_by_time()
	DP.retrospective_read()
	#DP.test()
	#TODO end of make method