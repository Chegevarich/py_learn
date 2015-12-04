#coding: utf-8
import xml.etree.ElementTree as ET
import sys

class make_xml_for_me():
	def __init__(self):
		self.events = []
		self.units = []
		self.coords = []

		self.all = {}


	def check_event(self, event):
		#TODO make real check
		if event not in self.events:
			self.add_event(event)
			self.check_event(event)
		elif event in self.events:
			return True

	def check_unit(self, unit):
		if unit not in self.units:
			self.add_unit(unit)
			self.check_unit(unit)
		elif unit in self.units:
			return True

	def add_unit(self, unit):
		self.units.append(unit)
		self.all[self.cur_event][unit] = []

	def add_event(self, event):
		self.events.append(event)
		self.all[event] = {}

	def add_coord_to_unit_event(self, event, unit, lng, lat, time):
		self.cur_event = event

		#print(event, unit, lng, lat, time)
		self.check_event(event)
		''' is not True:
			print(self.check_event(event) is not True)
			raise NameError('Sheeeeeee')
		'''
		#print(self.events)
		
		self.check_unit(unit)

		self.all[event][unit].append([lng, lat, time])

	def make_xml(self):
		root = ET.Element('root')

		for ei, e in enumerate(self.events):
			print(e)

			event = ET.SubElement(root, 'event')
			event.set('code', str(e))
			event.set('index', str(ei))

			for u in self.all[e]:
				print(u)

				unit = ET.SubElement(event, 'unit')
				unit.set('unit_code', str(u))

				for c in self.all[e][u]:
					print(c)

					coord = ET.SubElement(unit, 'coord')
					coord.set('lng',str(c[0]))
					coord.set('lnt',str(c[1]))
					coord.set('time',str(c[2]))


		ET.dump(root)		

	#def events_to_


if __name__ == '__main__':

	data = []

	events = ['just_first_event',]#'just_another_event',]
	units = ['first', 'secound', 'another', 'another22']
	start_on = [11.1, 11.1, 1447783306]

	for e in events:
		for u in units:
			for k in range(10):
				data.append([ e, u, start_on[0], start_on[1]+(k/10), start_on[2]+(k/10) ])

	#data.append(['just_first_event', 'another22', 22.34, 14.234, 1447783900])

	m = make_xml_for_me()

	for i in data:
		m.add_coord_to_unit_event(*i)

	#print(m.all)
	m.make_xml()
	#d event => unit => coords

	'''
	{
		'just_first_event': 
			{
				'secound': 
					[[12.3, 13.2, 1447783307], [13.3, 13.2, 1447783311], [14.3, 13.2, 1447783315], [15.3, 13.2, 1447783320], [16.3, 13.2, 1447783340], [17.3, 13.2, 1447783360], [18.3, 13.2, 1447783390], [19.3, 13.2, 1447783500], [20.3, 13.2, 1447783900]], 
				'first': 
					[[11.2, 11.3, 1447783306], [12.2, 11.3, 1447783311], [13.2, 11.3, 1447783315], [12.2, 11.3, 1447783320], [11.2, 11.3, 1447783340], [12.2, 11.3, 1447783360], [13.2, 11.3, 1447783390], [12.2, 11.3, 1447783500], [11.2, 11.3, 1447783900]], 
				'another': 
					[[13.434, 14.323, 1447783308], [14.434, 14.323, 1447783311], [15.434, 14.323, 1447783315], [16.434, 14.323, 1447783320], [17.434, 14.323, 1447783340], [18.434, 14.323, 1447783360], [19.434, 14.323, 1447783390], [20.434, 14.323, 1447783500], [21.434, 14.323, 1447783900]], 
				'another22': 
					[[14.34, 14.234, 1447783308], [15.34, 14.234, 1447783311], [16.34, 14.234, 1447783315], [17.34, 14.234, 1447783320], [18.34, 14.234, 1447783340], [19.34, 14.234, 1447783360], [20.34, 14.234, 1447783390], [21.34, 14.234, 1447783500], [22.34, 14.234, 1447783900]]
			}
	}  
	'''