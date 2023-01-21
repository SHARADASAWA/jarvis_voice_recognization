
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import datetime
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def greetme():
    hour=int(datetime.datetime.now().hour)    
    if hour>=0 and hour<=12:
        speak('good morning!')
    elif hour>=13 and hour<=18:
        speak('good afternoon!') 
    else:
         speak('good evening!')
    speak('i am jarvis sir  how can i help you')     
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:

         print('listening...')
         r.pause_threshold = 1
         audio = r.listen(source)
    try:
        print('recognising....')
        query=r.recognize_google(audio,language='en-in')
        print(f"USER said: {query}\n")
    except Exception as e:
        # print(e)    
        print("say that again please...")
        return"None"
    return query    


if __name__ =="__main__":
    greetme()
    while True:
        query= takecommand().lower()
        if 'wikipedia' in query:
            speak('searching...')
            query=query.replace("wikipedia","")
            results= wikipedia.summary(query,sentences=1)
            speak('according to wikipedia')
            print(results)
            speak(results)
        elif 'open youtube' in query :
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com") 
        elif 'the time' in query:
            strTime= datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")
        elif 'open chrome' in query:
            codepath="C:\Program Files\Google\Chrome\Application\chrome.exe"
            os.startfile(codepath)
        elif 'close' in query:
            exit




    




