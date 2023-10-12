from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Ellipse, Line, Color
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.animation import Animation
from kivy.config import Config

# screen config
Config.set('graphics', 'fullscreen', 'false')
Config.set('graphics', 'position', 'custom')
Config.set('graphics', 'left', 1780)
Config.set('graphics', 'top', 940)
Config.write()
Window.size = (110, 110)
Window.clearcolor = (1, 1, 1, 1)

class Najmaai(BoxLayout):
    def __init__(self, **kwargs):
        super(Najmaai, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.button = Button(text="")
        self.add_widget(self.button)
        self.button.bind(on_press=self.button_pressed)
        with self.canvas:
            self.eclipse = Ellipse(pos=(5, 5), size=(100, 100), source='../data/input/N.png')
            Color(0, 1, 1, 1)
            self.circle1 = Line(width=2, circle=(5 + 100 / 2, 5 + 100 / 2, 70 / 2))
            Color(1, 0, 1, 1)
            self.circle2 = Line(width=2, circle=(5 + 100 / 2, 5 + 100 / 2, 90 / 2))

    def button_pressed(self, instance):
        print("Button pressed!")

class MyApp(App):
    def build(self):
        return Najmaai()

if __name__ == '__main__':
    MyApp().run()
