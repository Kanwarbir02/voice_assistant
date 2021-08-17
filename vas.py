import pyttsx3 
import datetime

engine = pyttsx3.init()
engine.say("Hello I am Your Voice assistant")
engine.runAndWait()

print(datetime.datetime.now())