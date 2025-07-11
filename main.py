import pyttsx3
import speech_recognition as sr
import random
import webbrowser
import datetime 
from plyer import notification
import pyautogui
import wikipedia
import os
from openai import OpenAI

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 170)


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

client = OpenAI(
    base_url="https://api.a4f.co/v1",
    api_key="ddc-a4f-bc9c0045f80442948dc64deab05f5650"
)

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
        elif "say date" in request:
            now_date = datetime.datetime.now().strftime("%d/%m/%y")
            speak("current date is " + str(now_date))
        elif "new task" in request:
            task = request.replace("new task" , "")
            task = task.strip()
            if task != "":
                speak("Adding task : "+ task)
                with open ("todo.txt" , "a") as file:
                    file.write(task + "\n")
        elif "remove task" in request:
            task_to_remove = request.replace("remove task", "").strip()
            if task_to_remove == "":
                speak("Please specify the task you want to remove.")
                return
            try:
                with open("todo.txt", "r") as file:
                    tasks = file.readlines()
                tasks = [task for task in tasks if task.strip() != task_to_remove]

                with open("todo.txt", "w") as file:
                    file.writelines(tasks)
                speak(f"Removed task: {task_to_remove}")
            except FileNotFoundError:
                speak("To-do list file not found.")
        elif "speak task" in request:
            with open ("todo.txt" , "r") as file:
                speak("Work we have to do today is : " + file.read())
        elif "show work" in request:
            with open ("todo.txt" , "r") as file:
                tasks = file.read()
            notification.notify(
                title = "today's work",
                message = tasks
            )
        elif "open youtube" in request:
            speak("Opening Youtube")
            webbrowser.open("www.youtube.com")
        elif "open instagram" in request:
            speak("Opening instagram")
            webbrowser.open("www.instagram.com")
        elif "open snapchat" in request:
            speak("Opening snapchat")
            webbrowser.open("www.snapchat.com")
        elif "open google" in request:
            speak("Opening google")
            webbrowser.open("www.google.com")
        elif "open amazon" in request:
            speak("Opening amazon")
            webbrowser.open("www.amazon.com")
        elif "open" in request:
            query = request.replace("open" , "")
            pyautogui.press("super")
            pyautogui.typewrite(query)
            pyautogui.sleep(0.5)
            pyautogui.press("enter")
        elif "take a screenshot" in request.lower():
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            filename = f"screenshot_{timestamp}.png"
            try:
                screenshot = pyautogui.screenshot()
                screenshot.save(filename)
                speak("Screenshot taken and saved in this folder")
            except Exception as e:
                speak("Failed to take screenshot.")
                print("Error:", e)
        elif "wikipedia" in request:
            request = request.replace("jarvis" , "")
            request = request.replace("search wikipedia" , "")
            result = wikipedia.summary(request, sentences=3)
            print(result)
            speak(result)
        elif "google" in request:
            request = request.replace("jarvis" , "")
            request = request.replace("search google" , "")
            speak("searching " + request)
            webbrowser.open("https://www.google.com/search?q=" + request)
        elif "create an image" in request:
            request = request.replace("jarvis" , "")
            prompt_1 = request
            print("Creating image please wait.....")
            speak("Creating image please wait")
            img = client.images.generate(
                model="provider-3/FLUX.1-dev",
                prompt=prompt_1,
                n=1,
                response_format="url",
                size="1024x1024"
            )
            webbrowser.open(img.data[0].url)
        elif "chat" in request or "talk" in request or "say" in request:
            user_msg = request.replace("jarvis", "").replace("talk", "").replace("say", "").replace("chat" , "").strip()
            print("Showing result : ")
            resp = client.chat.completions.create(
                model="provider-6/gemini-2.5-flash-thinking",
                messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_msg}
                ],
                    stream=False
                )
            result = resp.choices[0].message.content
            print("Assistant:" , result)
            speak(result)
        



main_process()
