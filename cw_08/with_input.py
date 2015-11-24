#coding:utf-8
from kivy.app import App 
from kivy.uix.label import Label
from kivy.uix.image import Image, AsyncImage
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class Tst2App(App):
	def button_press(instance, value):
		print('My button <%s> state is <%s>' % (instance, value))

	def build(self):
 
		scroll = ScrollView()
		scroll.size = Window.size

		login_label = Label(text='Login')
		login_input = TextInput(text='', multiline=False)

		email_label = Label(text='Email')
		email_input = TextInput(text='', multiline=False)		

		pass_label = Label(text='Password')
		pass_input = TextInput(text='', multiline=False)		

		mainBox = BoxLayout(orientation='vertical')

		mainBox.add_widget(self.make_new_row([login_label,login_input]))
		mainBox.add_widget(self.make_new_row([email_label,email_input]))
		mainBox.add_widget(self.make_new_row([pass_label,pass_input]))

		button = Button(text='Hello world', font_size=14)		
		button.bind(on_press=self.button_press)

		mainBox.add_widget(self.make_new_row([button, ]))

		scroll.add_widget(mainBox)

		return scroll

	def make_new_row(self, list_or_elements):
		box = BoxLayout(orientation='horizontal')
		for i in list_or_elements:
			box.add_widget(i)
		return box

Tst2App().run()