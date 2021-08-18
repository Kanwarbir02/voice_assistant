import pyttsx3 
import speech_recognition as sr
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

def voiceInput():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        # r.pause_threshold=1
        # r.energy_threshold=300
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio)
        print(f"User said: {query}")

    except Exception as e:
        print(e)
        speak("Please try again, I could not listen properly.")     
        return "None" 
    return query

if __name__ == "__main__":
    voiceInput()