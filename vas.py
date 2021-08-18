import pyttsx3 
import datetime

engine = pyttsx3.init()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greet():
    currentHour = int(datetime.datetime.now().hour)
    if currentHour>0 and currentHour<12:
        speak("Good Morning Sir!")
    elif currentHour>12 and currentHour<16:
        speak("Good Afternoon Sir!")    
    else:
        speak("Good Evening Sir!")

    speak("How may I help you?")

if __name__ == "__main__":
    greet()