from kivy.app import App
from kivy.uix.button import Button
from kivy.config import Config
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scatter import Scatter

Config.set('graphics', 'resizeable', '0');
Config.set('graphics', 'width', '600');
Config.set('graphics', 'height', '900');

class MyApp(App):
    def build(self):
        s = Scatter()
        fl = FloatLayout(size = (300, 300))
        s.add_widget(fl)
        fl.add_widget(Button(
                    text = "First Button",
                    font_size = 16,
                    on_press = self.btn_press,
                    background_color = [1, 0, 0, 1],
                    background_normal = '',
                    size_hint = (.5, .25),
                    pos = (600//4, 900//2)));
        return s

    def btn_press(self, instance):
        print('Кнопка нажата!')
        instance.text = "IIIIII"

if __name__ == "__main__":
    MyApp().run()
