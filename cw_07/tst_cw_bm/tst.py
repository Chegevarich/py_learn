#coding:utf-8
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty


class Tst(Widget):
    inn = ObjectProperty(None)

    def __init__(self):
    	super().__init__()
    	self.inn.bind(text=self.on_text)

    def on_text(self, instance, value):
    	print(value)


class TstApp(App):

    def build(self):
        tst = Tst()
        return tst



if __name__ == '__main__':
    TstApp().run()