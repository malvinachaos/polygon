# Чтобы просто запустить приложение
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.config import Config
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

Config.set('graphics', 'resizeagle', '0');
Config.set('graphics', 'width', '600');
Config.set('graphics', 'height', '900');

# class Любое_словоApp(App)
class FunnyApp(App):
    def update_label(self):
        self.lbl.text = self.formula

    def add_number(self, instance):
        if (self.formula == "0"):
            self.formula = ''
        self.formula += str(instance.text)
        self.update_label()

    def add_operation(self, instance):
        self.formula += str(instance.text)
        self.update_label()

    def calc_result(self, instance):
        operators = ['*', '+', '-', '/']
        if "/0" in self.formula:
            self.lbl.text = "На ноль делить нельзя!"
        elif len(self.formula) % 2 == 0:
            self.lbl.text = "Выражение построено неправильно!"
        elif operators + operators in self.formula:
            self.lbl.text = "Выражение построено неправильно!"
        else:
            self.lbl.text = str(eval(self.lbl.text))
        self.formula = "0"

    def build(self):
        self.formula = "0"
        bl = BoxLayout(orientation = 'vertical', padding = 35)
        gl = GridLayout(cols = 4, spacing = 3, size_hint = (1, .6))

        self.lbl = (Label(text='0', font_size = 40, halign = "right", size_hint = (1, .4), text_size = (600 * .9, 900 * .25)))

        bl.add_widget(self.lbl)

        gl.add_widget(Button(text = "7", on_press = self.add_number))
        gl.add_widget(Button(text = "8", on_press = self.add_number))
        gl.add_widget(Button(text = "9", on_press = self.add_number))
        gl.add_widget(Button(text = "*", on_press = self.add_operation))

        gl.add_widget(Button(text = "4", on_press = self.add_number))
        gl.add_widget(Button(text = "5", on_press = self.add_number))
        gl.add_widget(Button(text = "6", on_press = self.add_number))
        gl.add_widget(Button(text = "-", on_press = self.add_operation))

        gl.add_widget(Button(text = "1", on_press = self.add_number))
        gl.add_widget(Button(text = "2", on_press = self.add_number))
        gl.add_widget(Button(text = "3", on_press = self.add_number))
        gl.add_widget(Button(text = "+", on_press = self.add_operation))

        gl.add_widget(Button(text = "0", on_press = self.add_number))
        gl.add_widget(Button(text = ".", on_press = self.add_number))
        gl.add_widget(Button(text = "=", on_press = self.calc_result))
        gl.add_widget(Button(text = "/", on_press = self.add_operation))

        bl.add_widget(gl)
        return bl


if __name__ == "__main__":
    FunnyApp().run()
