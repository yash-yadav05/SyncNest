import pyttsx3
import speech_recognition as sr
import random
import webbrowser
import datetime


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 190)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def command():
    content = " "
    while content == " ":
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source)

        try:
            content =  r.recognize_google(audio , language='en-in')
            print("You said..........." + content)
        except Exception as e:
            print("Please try again....😊")

    return content

def main_process():
    while True:
        request = command().lower()
        if "hello" in request:
            speak("Hii, How can i help you?")
        elif "play music" in request:
            speak("Playing music")
            song = random.randint(1,5)
            if song == 1:
                webbrowser.open("https://www.youtube.com/watch?v=Cb6wuzOurPc&list=RDCb6wuzOurPc&start_radio=1")
            elif song == 2:
                webbrowser.open("https://www.youtube.com/watch?v=kyjg5kX4pT0&list=RDkyjg5kX4pT0&start_radio=1")
            elif song == 3:
                webbrowser.open("https://www.youtube.com/watch?v=gkCKTuR-ECI&list=RDgkCKTuR-ECI&start_radio=1")    
            elif song == 4:
                webbrowser.open("https://www.youtube.com/watch?v=emh8zR4ZqZ0&list=RDemh8zR4ZqZ0&start_radio=1") 
            elif song == 5:
                webbrowser.open("https://www.youtube.com/watch?v=rS4G5az-MKA&list=RDrS4G5az-MKA&start_radio=1") 

        elif "say time" in request:
            now_time = datetime.datetime.now().strftime("%H:%M")
            speak("current time is " + str(now_time))


main_process()
