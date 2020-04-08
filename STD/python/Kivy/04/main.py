#! /bin/python3
from kivy.app import App
from kivy.graphics import Rectangle
from kivy.graphics import Color
from kivy.graphics import Line
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
# ---------------------------[Блок описания виджетов]--------------------------
# ------- Рисование
class Draw(Widget):
	choose_color = ObjectProperty(None)
	def __init__(self, **kwargs):
		super(Draw, self).__init__(**kwargs)
		self.btns = []
		clrs = [(1,1,1,1), (.75,.75,.75,1), (.5,.5,.5,1), (.25,.25,.25,1), (1,0,0,1), (.5,0,0,1), (0,1,0,1), (0,.5,0,1), (0,0,1,1),\
		        (0,0,.5,1), (1,1,0,1), (.5,.5,0,1), (0,1,1,1), (0,.5,.5,1), (1,0,1,1), (.5,0,.5,1)]
		for i, item in enumerate(clrs):
			BTN = Button(background_color=item)
			self.btns.append(BTN)
			self.choose_color.add_widget(self.btns[i])

		with self.canvas:
			Color(1,1,1,1, mode="rgba")
			self.LnE = Line(pos=(20,20, 40, 40))
			self.rect = Rectangle(pos=(20,20), size=(10,90))

		def on_touch_move(self, touch):
			self.LnE.pos = self.ln.pos, touch.pos
		def on_touch_down(self, touch):
			self.LnE.pos = 0,0

# ---------------------------[Блок запуска программы]--------------------------
class DrawingApp(App):
	def build(self):
		return Draw()

if __name__ == "__main__":
		DrawingApp().run()
