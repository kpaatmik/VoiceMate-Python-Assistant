#seting up jarvis
import pyttsx3
from decouple import config
from datetime import datetime
import speech_recognition as sr
from random import choice
from utils import opening_text
from functions.offilne import notepad,calculator,microsoftword,cmd


USERNAME=config('USERNAME')
BOTNAME=config('BOTNAME')
engine=pyttsx3.init('sapi5')
engine.setProperty('rate',190)
engine.setProperty('volume',1.0)
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

#setting up speak
def speak(text):
    engine.say(text)
    engine.runAndWait()
    
#greet user
def greet_user():
    hour=datetime.now().hour
    if((hour>=3)and(hour<12)):
        speak(f"Good morning{USERNAME}")
    elif((hour>=12)and(hour<19)):
        speak(f"Good afternoon{USERNAME}")
    elif((hour>=19)and(hour<24)):
        speak(f"Good Evening{USERNAME}")
    else:
        speak(f"Hey {USERNAME} it's really late,but iam here to assist you")
    speak(f"iam {BOTNAME} your personal assistant,ready to help you")
  
def take_user_input():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold=2
        audio=r.listen(source)
    try:
        print("Recognizing......")
        query=r.recognize_google(audio,language='en-in')
        if( not('exit' in query or 'stop' in query)):
            speak(choice(opening_text))
        else:
            hour = datetime.now().hour
            if hour >= 21 and hour < 6:
                speak("Good night sir, take care!")
            else:
                speak('Have a good day sir!')
            exit()
    except Exception:
        speak("Sorry i couldn't  understand that! Please say again.")
        query='None'
    return query

if __name__=='__main__':
    greet_user()
    while(True):
        query=take_user_input().lower()
        print(query)
        if(query!='none'):
            if('open notepad' in query):
                notepad()
            elif('open calculator' in query):
                calculator()
            elif('open word' in query):
                microsoftword()
            elif('open cmd' in query):
                cmd()
        else:
            break
      
