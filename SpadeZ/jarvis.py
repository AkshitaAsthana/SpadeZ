import time
from urllib import request
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr 
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
from ecapture import ecapture as ec
import wolframalpha
import subprocess
import time
import json
import requests
import pyjokes
import ctypes

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Spade Z. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        r.adjust_for_ambient_noise(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('thesky5515@gmail.com', 'naina5515')
    server.sendmail('akshitayou1@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   


        #elif 'play music' in query:
           # music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
      #     # songs = os.listdir(music_dir)
           # print(songs)    
           # os.startfile(os.path.join(music_dir, songs[0]))

        elif 'play despacito' in query:
            webbrowser.open("https://www.youtube.com/watch?v=kJQP7kiw5Fk&ab_channel=LuisFonsiVEVO")


        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\Akshita Asthana\AppData\Local\Programs\Microsoft VS Code\Code.exe"
            os.startfile(codePath)
        
        #elif 'open word' in query:
           # codePath = "C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE"
           # os.startfile(codePath)

       # elif 'open powerpoint' in query:
           # codePath = "C:\\Program Files\Microsoft Office\root\Office16\POWERPNT.exe"
           # os.startfile(codePath)

       # elif 'open VLC media player' in query:
           # codePath = "C:\\Program Files\VideoLAN\VLC\vlc.exe"
           # os.startfile(codePath)

       # elif 'open firefox' in query:
           # codePath = "C:\Program Files\Mozilla Firefox\firefox.exe"
           # os.startfile(codePath)

        elif 'tell me the latest news' in query:
            news = webbrowser.open("https://timesofindia.indiatimes.com/home/headlines")
            speak('Here are some headlines from the Times of India,Happy reading')
            time.sleep(6)

        elif "camera" in query or "take a photo" in query:
            ec.capture(0,"robo camera","img.jpg")

        elif 'ask' in query:
            speak('I can answer to computational and geographical questions  and what question do you want to ask now')
            question=takeCommand()
            app_id="7TVWY9-JEUPWJUYRY "
            client = wolframalpha.Client('R2K75H-7ELALHR35X')
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)

        elif "who i am" in query:
            speak("If you talk then definitely you are human.")
            print("If you talk then definitely you are human.")

        elif "why you came to world" in query:
            speak("Thanks to Akshita. further It's a secret")

        elif 'what is love' in query:
            speak("It is 7th sense that destroy all other senses")

        elif 'lock window' in query:
            speak("locking the device")
            ctypes.windll.user32.LockWorkStation()

        elif "don't listen" in query or "stop listening" in query:
            speak("for how much time you want to stop spade z from listening commands")
            a = int(takeCommand())
            time.sleep(a)
            print(a)

        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.nl/maps/place/" + location + "")

        elif 'joke' in query:
            speak(pyjokes.get_joke())
            print(pyjokes.get_joke())
 

        elif "weather" in query:
            api_key="a111e1ec3c620c74728f9e6ad0aa00d3"
            base_url="https://api.openweathermap.org/data/2.5/weather?"
            speak("what is the city name")
            city_name=takeCommand()
            complete_url=base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x=response.json()
            if x["cod"]!="404":
                y=x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))

      

        elif 'mail' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "akshitayou1@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend. I am not able to send this email") 

        elif 'who are you' in query or 'what can you do' in query:
            speak('I am Spade Z. I am programmed to minor tasks like'
                  'opening youtube,google chrome, gmail and stackoverflow ,predict time,take a photo,search wikipedia,predict weather' 
                  'In different cities, get top headline news from times of india and you can ask me computational or geographical questions too!')


        elif "who made you" in query or "who created you" in query or "who discovered you" in query:
            speak("I was built by Akshita, Naina and Yash")
            print("I was built by  Akshita, Naina and Yash")

        elif "log off" in query or "sign out" in query:
             speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
             subprocess.call(["shutdown", "/l"])
time.sleep(3)

        