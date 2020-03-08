# Чтобы просто запустить приложение
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.config import Config
from kivy.uix.widget import Widget
from kivy.uix.scatter import Scatter

Config.set('graphics', 'resizeable', '0');
Config.set('graphics', 'width', '600');
Config.set('graphics', 'height', '900');
# class Любое_словоApp(App)
class FunnyApp(App):
    def build(self):
        bl = GridLayout(cols = 4, padding = 30, spacing = 5)

        bl.add_widget(Button(text = "7"))
        bl.add_widget(Button(text = "8"))
        bl.add_widget(Button(text = "9"))
        bl.add_widget(Button(text = "*"))

        bl.add_widget(Button(text = "4"))
        bl.add_widget(Button(text = "5"))
        bl.add_widget(Button(text = "6"))
        bl.add_widget(Button(text = "-"))

        bl.add_widget(Button(text = "1"))
        bl.add_widget(Button(text = "2"))
        bl.add_widget(Button(text = "3"))
        bl.add_widget(Button(text = "+"))

        bl.add_widget(Widget())
        bl.add_widget(Button(text = "0"))
        bl.add_widget(Button(text = "."))
        bl.add_widget(Button(text = "="))

        return bl


if __name__ == "__main__":
    FunnyApp().run()
