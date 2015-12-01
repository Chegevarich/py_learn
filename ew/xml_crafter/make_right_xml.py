#coding: utf-8
import xml.etree.ElementTree as ET

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

	def add_event(self, event):
		self.events.append(event)

	def add_coord_to_unit_event(self, event, unit, lng, lat, time):
		#print(event, unit, lng, lat, time)
		self.check_event(event)
		''' is not True:
			print(self.check_event(event) is not True)
			raise NameError('Sheeeeeee')
		'''
		#print(self.events)
		
		self.check_unit(unit)

		self.all[event][unit].append(lng, lat, time)

	def make_xml():
		pass

	#def events_to_


if __name__ == '__main__':

	data = []

	data.append(['just_first_event', 'first', 11.2, 11.3, 1447783306 ])
	data.append(['just_first_event', 'first', 12.2, 11.3, 1447783311 ])
	data.append(['just_first_event', 'first', 13.2, 11.3, 1447783315 ])
	data.append(['just_first_event', 'first', 12.2, 11.3, 1447783320 ])
	data.append(['just_first_event', 'first', 11.2, 11.3, 1447783340 ])
	data.append(['just_first_event', 'first', 12.2, 11.3, 1447783360 ])
	data.append(['just_first_event', 'first', 13.2, 11.3, 1447783390 ])
	data.append(['just_first_event', 'first', 12.2, 11.3, 1447783500 ])
	data.append(['just_first_event', 'first', 11.2, 11.3, 1447783900 ])


	data.append(['just_first_event', 'secound', 12.3, 13.2, 1447783307])
	data.append(['just_first_event', 'secound', 13.3, 13.2, 1447783311])
	data.append(['just_first_event', 'secound', 14.3, 13.2, 1447783315])
	data.append(['just_first_event', 'secound', 15.3, 13.2, 1447783320])
	data.append(['just_first_event', 'secound', 16.3, 13.2, 1447783340])
	data.append(['just_first_event', 'secound', 17.3, 13.2, 1447783360])
	data.append(['just_first_event', 'secound', 18.3, 13.2, 1447783390])
	data.append(['just_first_event', 'secound', 19.3, 13.2, 1447783500])
	data.append(['just_first_event', 'secound', 20.3, 13.2, 1447783900])


	data.append(['just_first_event', 'another', 13.434, 14.323, 1447783308])
	data.append(['just_first_event', 'another', 14.434, 14.323, 1447783311])
	data.append(['just_first_event', 'another', 15.434, 14.323, 1447783315])
	data.append(['just_first_event', 'another', 16.434, 14.323, 1447783320])
	data.append(['just_first_event', 'another', 17.434, 14.323, 1447783340])
	data.append(['just_first_event', 'another', 18.434, 14.323, 1447783360])
	data.append(['just_first_event', 'another', 19.434, 14.323, 1447783390])
	data.append(['just_first_event', 'another', 20.434, 14.323, 1447783500])
	data.append(['just_first_event', 'another', 21.434, 14.323, 1447783900])


	data.append(['just_first_event', 'another22', 14.34, 14.234, 1447783308])
	data.append(['just_first_event', 'another22', 15.34, 14.234, 1447783311])
	data.append(['just_first_event', 'another22', 16.34, 14.234, 1447783315])
	data.append(['just_first_event', 'another22', 17.34, 14.234, 1447783320])
	data.append(['just_first_event', 'another22', 18.34, 14.234, 1447783340])
	data.append(['just_first_event', 'another22', 19.34, 14.234, 1447783360])
	data.append(['just_first_event', 'another22', 20.34, 14.234, 1447783390])
	data.append(['just_first_event', 'another22', 21.34, 14.234, 1447783500])
	data.append(['just_first_event', 'another22', 22.34, 14.234, 1447783900])


	m = make_xml_for_me()

	for i in data:
		m.add_coord_to_unit_event(*i)
	#d event => unit => coords

	#d_events[first_sample_event] = d_units[]
	'''
	      <event code='first_sample_event' index='0'>
	        <unit unit_code='first'>
	            <coord lng='11' lnt='11' time='1447783306'/>
	            <coord lng='12' lnt='11' time='1447783311'/>        
	            <coord lng='13' lnt='11' time='1447783315'/>
	            <coord lng='12' lnt='11' time='1447783320'/>
	            <coord lng='11' lnt='11' time='1447783340'/>
	            <coord lng='12' lnt='11' time='1447783360'/>
	            <coord lng='13' lnt='11' time='1447783390'/>
	            <coord lng='12' lnt='11' time='1447783500'/>
	            <coord lng='11' lnt='11' time='1447783900'/>
	        </unit>
	        <unit unit_code='secound'>
	            <coord lng='12' lnt='13' time='1447783307'/>
	            <coord lng='13' lnt='13' time='1447783311'/>        
	            <coord lng='14' lnt='13' time='1447783315'/>
	            <coord lng='15' lnt='13' time='1447783320'/>
	            <coord lng='16' lnt='13' time='1447783340'/>
	            <coord lng='17' lnt='13' time='1447783360'/>
	            <coord lng='18' lnt='13' time='1447783390'/>
	            <coord lng='19' lnt='13' time='1447783500'/>
	            <coord lng='20' lnt='13' time='1447783900'/>
	        </unit>            
	        <unit unit_code='another'>
	            <coord lng='13' lnt='14' time='1447783308'/>
	            <coord lng='14' lnt='14' time='1447783311'/>        
	            <coord lng='15' lnt='14' time='1447783315'/>
	            <coord lng='16' lnt='14' time='1447783320'/>
	            <coord lng='17' lnt='14' time='1447783340'/>
	            <coord lng='18' lnt='14' time='1447783360'/>
	            <coord lng='19' lnt='14' time='1447783390'/>
	            <coord lng='20' lnt='14' time='1447783500'/>
	            <coord lng='21' lnt='14' time='1447783900'/>
	        </unit>            
	        <unit unit_code='another22'>
	            <coord lng='14' lnt='14' time='1447783308'/>
	            <coord lng='15' lnt='14' time='1447783311'/>        
	            <coord lng='16' lnt='14' time='1447783315'/>
	            <coord lng='17' lnt='14' time='1447783320'/>
	            <coord lng='18' lnt='14' time='1447783340'/>
	            <coord lng='19' lnt='14' time='1447783360'/>
	            <coord lng='20' lnt='14' time='1447783390'/>
	            <coord lng='21' lnt='14' time='1447783500'/>
	            <coord lng='22' lnt='14' time='1447783900'/>
	        </unit>    
	      </event>
	'''






'''

	root = ET.Element('root')

	event = ET.SubElement(root, 'event')
	unit = ET.SubElement(event, 'unit')

	c = ET.SubElement(unit, 'coord')
	c.set('updated', 'yes')

	ET.SubElement(unit, 'coord')
	ET.SubElement(unit, 'coord')
	ET.SubElement(unit, 'coord')
	ET.SubElement(unit, 'coord')
	ET.SubElement(unit, 'coord')
	ET.SubElement(unit, 'coord')


	ET.dump(root)
'''