#! /usr/bin/python3
'''
    Про kv файлы. Имя кв-файла создаётся по следующим правилам:
    1) Название в нижнем регистре
    2) Оно содержит только название основного класса, где приложение собирается
    3) Если название оканчивается на 'app', то пишем без него
    
    Пример:
    class MyApp() --> my.lv
    class TELEPHONE() --> telephone.kv
'''
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
# Этот модуль позволить использовать функции/переменный из нашего python скрипта
# в kv файле
from kivy.properties import ObjectProperty

class MyWidget(Widget):
    # Задаём переменные
    text1 = ObjectProperty(None)
    text2 = ObjectProperty(None)
    
    def ded(self, instance):
        self.remove_widget(self.btn)
    def press(self):
        print("Heh, {}.\nI guess, that is your\'s: {}".format(self.text1.text,\
                self.text2.text))
        self.text1.text, self.text2.text = '', ''
        self.btn = Button(text = "PRESS 'OK', IF YOU ARE NOT EATING COOKIES!")
        self.btn.size = self.width * .75, self.height
        self.btn.background_normal = "icon.png"
        self.btn.bind(on_press = self.ded) 
        self.add_widget(self.btn)


class MyApp(App):
    def build(self):
        return MyWidget()

if __name__ == "__main__":
    MyApp().run()
