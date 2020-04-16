#! /usr/bin/python3
from kivy.app import App
# Для того, чтобы загружать любые kv файлы
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


# ---------------------------[Экраны]------------------------------------------
# Для каждого экрана свой класс
# Для управлением более одного экрана нам понадобится организовать перемещение
# между ними.

class Menu(Screen):
	pass

class Second(Screen):
	pass

class WindowManager(ScreenManager):
	pass

# ---------------------------[Главный исполнительный блок]---------------------
# В Kivy есть такая штука, как builder. С её помощью мы можем загрузить любой
# нужный нам kv файл. Это избавляет нас от изрващений с именами kv файлов.
kv = Builder.load_file("my.kv")

class UnicornApp(App):
	def build(self):
		# И, соответственно, мы возвращаем переменную с настройками "my.kv"
		return kv


if __name__ == "__main__":
		UnicornApp().run()
