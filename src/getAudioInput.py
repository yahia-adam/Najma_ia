import speech_recognition as sr

r = sr.Recognizer()

def get_audio_input():
    with sr.Microphone() as source:
        print("Say something ...")
        print(">>>", end="")
        audio=r.listen(source)
    try:
        requiest = r.recognize_google(audio)
    except:
        requiest = ""
    return requiest
