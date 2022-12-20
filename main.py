import speech_recognition as sr
import pyttsx3
import os
from date_time import get_time, get_date
from lists import*

reco = sr.Recognizer()

engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[-2].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

while True:

    with sr.Microphone() as source:
        audio = reco.listen(source)

        speech = reco.recognize_google(audio, language='pt')
        if speech in time_list:
            time = get_time()
            speak(time)
        elif speech in date_list:
            date = get_date()
            speak(date)
        elif speech in notepad_list:
            speak("Abrindo Notepad")
            os.system('notepad.exe')
        elif speech in chorme_list:
            speak("Abrindo Google Chrome")
            os.system('"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"')
        else:
            print(speech)
            speak("Não entendi oque você disse")