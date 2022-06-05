import pyttsx3
import datetime

def Say(text):
    engine = pyttsx3.init('sapi5')
    engine.setProperty('rate', 160)
    engine.setProperty('volume', 0.8)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    print(f'Future : {text}\n')
    engine.say(str(text))
    engine.runAndWait()

def wishMe():
     hour = int(datetime.datetime.now().hour)
     if hour>=0 and hour<12:
         Say("Good Morning Sir! Tell me How can I help You ?")
     elif hour>=12 and hour<18:
         Say("Good Afternoon Sir! Tell me How can I help You ?")
     else:
        Say("Good Evening Sir! Tell me How can I help You ?")


