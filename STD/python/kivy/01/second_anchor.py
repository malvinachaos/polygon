# Чтобы просто запустить приложение
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput

# class Любое_словоApp(App)
class FunnyApp(App):
    def build(self):
        al = AnchorLayout(anchor_x = left)

        bl = BoxLayout(orientation = 'vertical', size_hint=[.4,.4])
        bl.add_widget(TextInput())
        bl.add_widget(Button(text="X"))

        al.add_widget(bl)
        return al


if __name__ == "__main__":
    FunnyApp().run()
