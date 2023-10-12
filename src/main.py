
from kivy.app import App
from kivy.lang import Builder
from kivy.config import Config
from kivy.core.window import Window
from kivy.animation import Animation

# screen config

Config.set('graphics', 'position', 'custom')
Config.set('graphics','top', 0)
Config.set('graphics','left', 0)
Config.set("graphics", "resizable", 0)
Config.set("graphics", "fullscreen", 0)

Window.size = (140, 140)
Window.clearcolor = (1, 1, 1, 1)

class Najma(App):
    def build(self):
        return Builder.load_file("/home/najma/Documents/adam.ai.student/najma-ia/src/kivyfile/main.kv")

    def myanimation(self, widget, *args):
        anim = Animation(opacity=0, duration=0.5)
        anim += Animation(opacity=1, duration=3)
        anim.start(widget)

Najma().run()

# import file
# from getAudioInput import get_audio_input
# from getWrittenInput import get_written_input
# from askOpenAi import ask_openai
# from execCommandLine import exec_command_line
# if __name__ == "__main__":    
    # while True:
    #     print("1 for speech and 2 for text ...")
    #     print(">>>",end="")
    #     text_or_audio = input()

    #     if (text_or_audio == "1"):
    #         message = get_audio_input()
    #         answer = ask_openai(message)
    #         print(f"Answer: >>>{answer}<<<")
    #         exec_command_line(answer)
    #     elif (text_or_audio == "2"):
    #         message = get_written_input()
    #         answer = ask_openai(message)
    #         print(f"Answer: >>>{answer}<<<")
    #         exec_command_line(answer)
