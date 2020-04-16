#! /usr/bin/python3
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.properties import ObjectProperty

class PRess(Widget):
	def btn(self):
		show_popup()

class Pi(FloatLayout):
	pass

kv = Builder.load_file("POPUP.kv")

class Unicorn(App):
	def build(self):
		return PRess()

def show_popup():
	# Создание popup окна
	show = Pi()
	popupWindow = Popup(title="Popup window", content=show, \
					    size_hint=(None, None), size=(400, 400))
	# Показывает контент
	popupWindow.open()


if __name__ == "__main__":
		Unicorn().run()
