#! /usr/bin/python3

# ---------------------------[IMPORT]------------------------------------------
from kivymd.app import MDApp
from kivy.base import EventLoop

#       -------------------~~~ UIX ~~~-------------------
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.button import MDFlatButton
from kivymd.uix.button import MDRoundFlatButton
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.card import MDCard
from kivymd.uix.card import MDSeparator

from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivy.config import Config
# -----------------------------------------------------------------------------

Config.set('kivy', 'keyboard_mode', 'systemanddock')
Window.size = (480, 853) # 720, 1280

class FirstScreen(Screen):
    pass

class Container(Screen):
    tomboy = ObjectProperty()
    l_widget = ObjectProperty()
    clear_button = ObjectProperty()
    def ch_text(self):
        self.l_widget.text = self.tomboy.text.upper()
    def cls_text(self):
        self.tomboy.text, self.l_widget.text = 'NEED TOMBOY', ''


class ThirdScreen(Screen):
    pass

class DragonApp(MDApp):
    title = 'DRAGON SUPER APP'
    def build(self):
        # you need conect ObjectProperty
        self.theme_cls.primary_palette = "Pink"
        sm = ScreenManager()
        sm.add_widget(FirstScreen())
        sm.add_widget(Container())
        sm.add_widget(ThirdScreen(name="NUDES"))
        return sm

if __name__ == '__main__':
    DragonApp().run()


'''
    Available palletes
    ‘Red’, ‘Pink’, ‘Purple’, ‘DeepPurple’, ‘Indigo’, ‘Blue’, ‘LightBlue’,
    ‘Cyan’, ‘Teal’, ‘Green’, ‘LightGreen’, ‘Lime’, ‘Yellow’, ‘Amber’, ‘Orange’,
    ‘DeepOrange’, ‘Brown’,
    ‘Gray’, ‘BlueGray’.
'''
