import pyttsx3 
import speech_recognition as sr
import datetime
import wikipedia
from selenium import webdriver
import webbrowser

engine = pyttsx3.init()







def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greet():
    currentHour = int(datetime.datetime.now().hour)
    if currentHour>4 and currentHour<12:
        speak("Good Morning Sir!")
    elif currentHour>=12 and currentHour<16:
        speak("Good Afternoon Sir!")    
    elif currentHour>=16 and currentHour<=17:
        speak("Good Evening Sir!")
    else:
        speak("Greetings Sir!")    

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
    greet()
    while True:
        query = voiceInput().lower()

        if "wikipedia" in query:
            speak("Searching Wikipedia")
            query.replace("wikipeida", " ")
            result = wikipedia.summary(query, sentences=2)
            print(result)
            speak(f"According to wikipedia {result}")

        elif "open google" in query:
            webbrowser.open("google.com")
        elif "open youtube" in query:
            webbrowser.open("youtube.com")
        elif "open spotify" in query:
            webbrowser.open("spotify.com")
        elif "open discord" in query:
            webbrowser.open("discord.com")  

        elif "the time" in query:
            strTime = datetime.datetime.strftime("%H:%M:%S")
            speak(strTime)
        elif "the date" in query:
            strDate = datetime.date.today() 
            speak(strDate)   


        elif "quit" in query:
            break        
            
           