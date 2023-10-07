import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Hi i'am najma-ai, how can i help you ?")
    audio=r.listen(source)
    print("Time Over...")

try:
    requiest = r.recognize_google(audio)
except:
    print("Didn't understand the audio")