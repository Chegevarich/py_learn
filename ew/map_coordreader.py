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

	def pop_ups(self, *args):
		self.mapview.add_marker(MapMarkerPopup(lat=50.4394,lon=3.017))
		print('pop_ups')

	def __init__(self, DP):
		self.DP = DP
		super().__init__()

	def build(self):

		mainBox = BoxLayout(orientation='vertical')

		
		#mainBox.add_widget(map_source)
		self.mapview = MapView()
		self.mapview.lat = 50.6394
		self.mapview.lon = 3.057
		self.mapview.zoom = 13
		self.mapview.map_source = MapSource(sys.argv[1], attribution="") if len(sys.argv) > 1 else "osm"

		mainBox.add_widget(self.mapview)

		self.mapview.add_marker(MapMarkerPopup(lat=50.6394,lon=3.057))
		#self.mapview.add_marker(MapMarkerPopup(lat=50.4394,lon=3.017))

		#mapmarkerpopup = MapMarkerPopup()

		if self.i < 5:
			self.i+=1
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
