#coding:utf-8
from kivy.app import App 
from kivy.uix.label import Label
from kivy.uix.image import Image, AsyncImage
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout

class Tst2App(App):
	def add_block(self, i):
		b = BoxLayout(original='horizontal')

		if i%2:
			image = AsyncImage(source='http://i3.kym-cdn.com/entries/icons/original/000/016/925/498ed76be651cffb6bb9bac6a9bb75c3.png', allow_stretch=True, keep_ratio=True)
			text = Label(text='brutalText')
		else :
			image = Image(source='img.jpg', keep_ratio=True, allow_stretch=True)
			text = Label(text='not so brutalText')

		b.size = ( 300, 150 )

		b.add_widget(image)
		b.add_widget(text)

		b.size_hint = (None, None)

		return b

	def make_scroll(self):
		scroll = ScrollView( )

		box = BoxLayout( orientation='vertical')

		height = 0
		for i in range(10):
			b = self.add_block(i)
			height += b.height
			box.add_widget( b )

		box.size=300, height
		scroll.size=Window.size
		box.size_hint_y = None
		scroll.add_widget(box)

		return scroll

	def build(self):
		box = BoxLayout(orientation='horizontal')

		for i in range(5):
			box.add_widget(self.make_scroll())
 
		return box

Tst2App().run()