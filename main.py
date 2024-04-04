import speech_recognition as sr
import pyttsx3 as p
import webbrowser
import os
import datetime
import subprocess
import wikipedia
from ecapture import ecapture as ecp
import subprocess
import pyjokes
import json
import wolframalpha
import requests
import time
import pywhatkit

print("Loading your personal assistant....Please wait....")

engine = p.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('Voice', voices[1].id)

def speak(txt):
    engine.say(txt)
    engine.runAndWait()

def Wish():
      hour = datetime.datetime.now().hour
      if hour>=0 and hour<12:
            speak("Hello!!Good Morning")
            print("Hello!!Good Morning")
      elif hour>=12 and hour<16:
            speak("Hello!! Good Afternoon")
            print("Hello!!Good Afternoon")
      else:
            speak("Hello!!Good Evening")
            print("Hello!!Good Evening")

def Command():
    s = sr.Recognizer()

    with sr.Microphone() as source:
        s.energy_threshold = 10000
        s.adjust_for_ambient_noise(source,1.2)
        print("Listening....")
        aud = s.listen(source)

    try:
        txt = s.recognize_google(aud, language = "en-in")
        print(f"user said: {txt}\n")

    except Exception as exp:
         speak("Did not get you....please speak again??")
         return "None"
    return txt

speak ("Loading your personal assistant....Please Wait..")
Wish()


if __name__ == '__main__':
     
    while True:
        speak("I am ProAssist,How may I help you today?")
        txt = Command().lower()
        if txt == 0:
            continue
        
        if "bye" in txt or "stop" in txt or "thank you" in txt:
            speak('It was my pleasure helping you...hope you have a great day ahead')
            print('It was my pleasure helping you..hope you have a great day ahead')
            break
          
        
        
        if 'wikipedia' in txt:
            speak('searching wikipedia now...')
            txt = txt.replace("wikipedia", " ")
            result = wikipedia.summary(txt , sentences=3)
            speak("According to wikipedia")
            speak(result)
            print(result)

        elif 'open youtube' in txt:
             webbrowser.open_new_tab("https://www.youtube.com")
             print('recognising....')
             speak('Opening Youtube now...')
             time.sleep(5)

        elif 'open google chrome' in txt:
             webbrowser.open_new_tab("https://www.google.com")
             print('recognising....')
             speak("Opening Google Chrome now...")
             time.sleep(5)
             
        elif 'open gmail' in txt:
             webbrowser.open_new_tab('gmail.com')
             print('recognising....')
             speak("Opening Gmail now...")
             time.sleep(5)
        
        elif 'time' in txt:
             stTime = datetime.datetime.now().strftime("%H:%M:%S")
             speak (f"The time now is {stTime}")

        elif 'news' in txt:
             news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
             speak("Here are some trending headlines for you from Times of India,happy reading.")
             time.sleep(5)
   
        elif 'ask' in txt:
             speak("Yes,sure...I can answer computational and geographical questions.")
             question = Command()
             app_id = "LEYVQ3-39LP2W98R4"
             client = wolframalpha.Client('LEYVQ3-39LP2W98R4')
             res = client.query(question)
             ans = next(res.results).text
             speak(ans)
             print(ans)

        elif 'play music' in txt: 
             speak("What music do you want to play??.....")
             qr = Command()
             speak("Playing now....")
             pywhatkit.playonyt(qr)
             while qr == None:
                  speak("Sorry did not get you...Please say that again")
                  continue
             
             
 
        elif "camera" in txt or "take a photo of me" in txt:
             ecp.capture(0,"robo camera","img.jpg")
        


        


