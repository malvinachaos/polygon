# Чтобы просто запустить приложение
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

# class Любое_словоApp(App)
class FunnyApp(App):
    def build(self):
        bl = BoxLayout(orientation = "vertical", padding = [50, 25, 10, 100], spacing = 5)
        bl.add_widget(Button(text = "One"))
        bl.add_widget(Button(text = "Two"))
        bl.add_widget(Button(text = "Three"))
        bl.add_widget(Button(text = "Four"))

        return bl


if __name__ == "__main__":
    FunnyApp().run()
