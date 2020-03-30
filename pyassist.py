import pyautogui
import time
import pyttsx3
import wikipedia
from datetime import datetime
import webbrowser
import pyaudio
import os
import smtplib
import speech_recognition as sr
engine=pyttsx3.init()
engine.say("Initializing Py-Assist.....")
engine.runAndWait()
hour=datetime.now().hour
if hour<12:
    engine.say("Good Morning Sir")
    engine.runAndWait()
elif hour>=12 and hour<16:
    engine.say("Good Afternoon Sir")
    engine.runAndWait()
elif hour>=16:
    engine.say("Good Evening Sir")
    engine.runAndWait()
t="now it is "+datetime.now().strftime("%H")+" "+datetime.now().strftime("%M")
engine.say(t)
engine.say("Give Identity...")
engine.runAndWait()
r=sr.Recognizer()
auth="ab"
with sr.Microphone() as source:
    try:
        identity=r.listen(source,2,10)
        auth=r.recognize_google(identity)
        print(auth)
    except:
        print:"Authentication Failed!!"
    if "what's up" in auth.lower():
        engine.say("authentication successful")
        engine.runAndWait()
        engine.say("How may i help you?")
        engine.runAndWait()
        text="abcd"
        while "bye" not in text.lower():
            text="abcd"
            with sr.Microphone() as source:
                audio=r.listen(source,2,10)
                try:
                    text=r.recognize_google(audio)
                    print(text)
                except:
                    print("Sorry not clear!!")
                    continue
                if "hello" in text.lower() or "hey" in text.lower():
                    engine.say("Hello Sir")
                    engine.runAndWait()
                elif "wikipedia" in text.lower():
                    text=text.replace("Wikipedia","")
                    engine.say("Searching wikipedia...")
                    engine.runAndWait()
                    query=wikipedia.summary(text,sentences=2)
                    print(query)
                    engine.setProperty('rate',150)
                    engine.say(query)
                    engine.runAndWait()
                    engine.setProperty('rate',200)
                elif "youtube" in text.lower():
                    webbrowser.open("youtube.com")
                    time.sleep(3)
                    engine.say("Say name of the video")
                    engine.runAndWait()
                    try:
                        video=r.listen(source,2,10)
                        vname=r.recognize_google(video)
                        print(vname)
                        pyautogui.typewrite(vname,0.2)
                        pyautogui.press('enter')
                        time.sleep(4)
                        pyautogui.click(250,501,1,0.2)
                    except:
                        engine.say("You did not speak")
                        engine.runAndWait()
                elif "google" in text.lower():
                    webbrowser.open("google.com")
                    time.sleep(3)
                    engine.say("Say your query")
                    engine.runAndWait()
                    try:
                        video=r.listen(source,2,10)
                        vname=r.recognize_google(video)
                        print(vname)
                        pyautogui.typewrite(vname,0.2)
                        pyautogui.press('enter')
                    except:
                        engine.say("You did not speak")
                        engine.runAndWait()
                elif "volume" in text.lower():
                    if "lower" in text.lower() or "low" in text.lower() or "decrease" in text.lower():
                        pyautogui.press('down',presses=5)
                    elif "higher" in text.lower() or "high" in text.lower() or "increase" in text.lower():
                        pyautogui.press('up',presses=5)
                elif "bye" in text.lower():
                    engine.say("Goodbye Sir")
                    engine.runAndWait()
                elif "time" in text.lower():
                    t="now it is "+datetime.now().strftime("%H")+" "+datetime.now().strftime("%M")
                    engine.say(t)
                    engine.runAndWait()
                elif "minecraft" in text.lower():
                    os.popen('C:\\Users\\Monty\\AppData\\Roaming\\.minecraft\\TLauncher.exe')
                elif "paint" in text.lower():
                    os.popen("maspaint.exe")
                elif 
                else :
                    engine.say("Keyword missing")
                    engine.runAndWait()
    else:
        print("Authentication Failed!!")
        engine.say("Authentication Failed!")
        engine.runAndWait()
        




