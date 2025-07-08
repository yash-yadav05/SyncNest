import pyttsx3
import speech_recognition as sr
import random
import webbrowser
import datetime 
from plyer import notification
import pyautogui

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

            




main_process()
