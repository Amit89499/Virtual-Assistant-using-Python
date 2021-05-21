# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pyttsx3
import datetime
import pywhatkit
import speech_recognition as sr
import wikipedia
import pyjokes
import webbrowser
import os
import time
import smtplib
engine=pyttsx3.init('sapi5') # sapi5 helps in synthesis and recognition of voice. Microsoft developed speech api
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

# Now, we will write our speak() function to convert our text to speech.
def speak(audio):
    engine.say(audio)
    engine.runAndWait() # without this command,speech will not be audible to us
    
def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Amit!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon Amit!")
    else:
        speak("Good Evening Amit!")
    
    speak(" I am Your Personal Assistant sir. Please tell me how may i help you")

def takeCommand():
    # It takes microphone input from the user and returns string output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening.......")
        r.adjust_for_ambient_noise(source,duration=1)
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recogning........")
        query=r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please.......")
        return "None"
    return query

def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()   # to connect our server to gmail server......
    server.starttls()   # to provide security.....
    server.login('youremail@gmail.com','passwd')
    server.sendmail("youremail@gmail.com",to,content)
    server.close()
        


if __name__ == '__main__':
    #wishMe()
    while True:
        query=takeCommand().lower()
        # logic for executing tasks based on query
        # browsing on wikipedia...........
        if 'wikipedia' in query:
            speak("Searching Wikipedia.....")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        # browsing on youtube............
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        # browsing on google
        elif 'open google' in query:
            webbrowser.open("google.com")
        # getting the current time
        elif 'the time' in query:
            time=datetime.datetime.now().time("%H:%M:%S")
            speak(f"Sir the time is {time}")
        # Playing music on youtube
        elif 'play' in query:
            song=query.replace('play','')
            speak('playing'+song)
            pywhatkit.playonyt(song)
        # to open the code editor
        elif 'open sublime' in query:
            codePath="C:\\Program Files\\Sublime Text 3\\sublime_text.exe"
            os.startfile(codePath)
        # to get the jokes
        elif 'joke' in query:
            speak(pyjokes.get_joke())

        # sending an email
        elif 'email' in query:
            try:
                speak("What should I say?")
                content=takeCommand()
                to="recieversmail@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry I am not able to send this email")
        # to shut down the Laptop
        elif 'shut down' in query:
            speak("Shutting the computer")
            os.system("shutdown /s /t 30")
            break
        