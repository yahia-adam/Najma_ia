import speech_recognition as sr

r = sr.Recognizer()

def get_user_input():
    with sr.Microphone() as source:
        print("Hi i'am najma-ai, how can i help you ?")
        audio=r.listen(source)
    try:
        requiest = r.recognize_google(audio)
        return requiest
    except:
        return None
