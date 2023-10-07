from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button

class Najma(App):
    def build(self): 
        return Button(text='Hello world', font_size=14)

if __name__ == "__main__":
    Najma().run()