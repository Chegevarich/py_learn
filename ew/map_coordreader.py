from coordreader import DataProvider
import sys

from kivy.base import runTouchApp
from kivy.lang import Builder

from kivy.clock import Clock

from kivy.app import App 
from kivy.uix.image import Image, AsyncImage
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.garden.mapview import MapView, MapSource, MapMarkerPopup

class Tst2App(App):

	i = 0

	def run(self):
		super().run()

	def add_new_marker(self, lat, lon, unit_name):
		print("add_new_marker")
		self.units_markers[unit_name] = MapMarkerPopup(lat=float(lat),lon=float(lon))
		self.mapview.add_marker( self.units_markers[unit_name] )


	def pop_ups(self, *args):

		self.gagarin.lat+=0.01
		self.gagarin.lon+=0.01

		if str(self.DP.start_time+self.iter) in self.DP.coords_by_time_dict:
			for i in self.DP.coords_by_time_dict[str(self.DP.start_time+self.iter)]:

				if self.units_markers[i[0]] == None:
					self.add_new_marker(i[1][0], i[1][1], i[0])
				else:
					self.units_markers[i[0]].lat = float(i[1][0])
					self.units_markers[i[0]].lon = float(i[1][1])
		#TODO lear how to right 
		self.mapview.do_update(None)

		self.iter+=1
		print('pop_ups', self.iter)

	def __init__(self, DP):
		#prepare work with data
		self.units_markers = {}
		self.DP = DP

		#все описанные unit's in a list
		self.units = list(self.DP.coord_array.keys())

		#just prepare
		for i in self.units:
			self.units_markers[i] = None


		super().__init__()

	def build(self):

		self.iter = 0

		mainBox = BoxLayout(orientation='vertical')

		
		#mainBox.add_widget(map_source)
		self.mapview = MapView()
		self.mapview.lat = 50.6394
		self.mapview.lon = 3.057
		self.mapview.zoom = 13

		self.mapview.map_source = MapSource(sys.argv[1], attribution="") if len(sys.argv) > 1 else "osm"

		mainBox.add_widget(self.mapview)

		#dirty learn :()
		#print( dir(self.mapview) )

		self.gagarin = MapMarkerPopup(lat=50.6394,lon=3.057)
		self.mapview.add_marker( self.gagarin )
		#self.mapview.add_marker(MapMarkerPopup(lat=50.4394,lon=3.017))

		#mapmarkerpopup = MapMarkerPopup()

		Clock.schedule_interval(self.pop_ups, 1)

		return mainBox

		def mapMarkerPopup(self):
			pass
			label = Label(text="[b]Lille[/b]\\n1 154 861 hab\\n5 759 hab./km2", markup=True, haligh="center")
			image = AsyncImage(source="http://upload.wikimedia.org/wikipedia/commons/9/9d/France-Lille-VieilleBourse-FacadeGrandPlace.jpg", mipmap=True)
			box = BoxLayout(orientation="horizontal", padding="5dp")
			box.add_widget(label)
			box.add_widget(image)

			

			return box


if __name__=='__main__':
	DP = DataProvider('first_sample_event', 1, './sample_data/sample_event0.xml')
	DP.xml_full_prepare()

	#for i in DP.retrospective_read():
		#print(i)

	T = Tst2App(DP)
	T.run()
