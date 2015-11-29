from kivy.app import App
from kivy.uix.widget import Widget

class Tst(Widget):
    pass

class TstApp(App):
    def build(self):
        tst = Tst()
        print(tst.size)
        return tst

if __name__ == '__main__':
    TstApp().run()