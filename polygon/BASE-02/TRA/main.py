#! /usr/bin/python3
from kivy.app import App
from kivy.lang import Builder
from kivy.base import EventLoop
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image


#kv = Builder.load_file("TRA.kv")
# ---------------------------[Окна]--------------------------------------------
class MainMenu(Screen):
	pass

class PartyMenu(Screen):
	pass

'''
class PlayersMenu(Screen):
	pass

class PlayerEditor(Screen):
	pass

class Game(Screen):
 	pass

'''
class WindowManager(ScreenManager):
	pass
# ---------------------------[Главный исполнительный блок]---------------------
kv = Builder.load_file("BACK.kv")

class DragonApp(App):
	def build(self):
		return kv

if __name__ == "__main__":
		DragonApp().run()
