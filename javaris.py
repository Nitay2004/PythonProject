# Author:- Nitay , Yash.........
# Date:- 21 -07-2023..............
# Topic:- AI bot TAPU...............

import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os


engine  = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')

# print(voices[0].id)
engine.setProperty('voices' , voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        speak("Good Morning!")

    elif hour>= 12 and hour<18:
        speak("Good Afternoon!")
    
    else:
        speak("Good Evening!")
    
    speak("I am Tapu how can I help you ")

def takecommand():
        # take command from mic 

        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening.......")
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            print("Recognising.....")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")

        except Exception as e:
            print(e)
            print("Say that again please.......")
            return "None"
        
        return query



if __name__ == "__main__":
        wishMe()
        # while True:
        if 1:
            query = takecommand().lower()

            # Logic for executing tasks based on query
            if 'wikipedia' in query:
                 speak('Searching wikipedia.....')
                 query = query.replace("wikipedia" , "")
                 results = wikipedia.summary(query , sentences = 2)
                 speak("According to wikipedia")
                 print(results)
                 speak(results)

            elif 'open youtube' in query:
                webbrowser.open("youtube.com")

            elif 'open google' in query:
                webbrowser.open("google.com")
            
            elif 'open stackoverflow' in query:
                webbrowser.open("stackoverflow.com")

            elif 'play music' in query:
                 music_dir = 'E:\Bdiya Gaaanne'
                 songs = os.listdir(music_dir)
                 print(songs)
                 os.startfile(os.path.join(music_dir , songs[0]))

            elif 'the time' in query:
                 strTime = datetime.datetime.now().strftime("%H:%M:%S")
                 speak (F"Sir the time is {strTime}")

            elif 'open code' in query:
                 codePath = "C:\\Users\\Nitay Verma\\AppData\Local\\Programs\\Microsoft VS Code\\Code.exe"
                 os.startfile(codePath)

            # elif 'send email' in query:
            #      try:
            #           speak("What should I say?")
            #           content = takecommand()
            #           to = ""                     
            #        #  sendEmail(to , content)