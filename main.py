# import datetime
# import os
# import sys
# import time
# import webbrowser
# import pyautogui
# import pyttsx3
# import speech_recognition as sr
# import json
# import pickle
# from tensorflow.keras.models import load_model
# from tensorflow.keras.preprocessing.sequence import pad_sequences
# import random
# import numpy as np
# import psutil 
# import subprocess


# with open("intents.json") as file:
#     data = json.load(file)

# model = load_model("chat_model.h5")

# with open("tokenizer.pkl", "rb") as f:
#     tokenizer=pickle.load(f)

# with open("label_encoder.pkl", "rb") as encoder_file:
#     label_encoder=pickle.load(encoder_file)

# def initialize_engine():
#     engine = pyttsx3.init("sapi5")
#     voices = engine.getProperty('voices')
#     engine.setProperty('voice', voices[1].id)
#     rate = engine.getProperty('rate')
#     engine.setProperty('rate', rate-50)
#     volume = engine.getProperty('volume')
#     engine.setProperty('volume', volume+0.25)
#     return engine

# def speak(text):
#     engine = initialize_engine()
#     engine.say(text)
#     engine.runAndWait()

# def command():
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         r.adjust_for_ambient_noise(source, duration=0.5)
#         print("Listening.......", end="", flush=True)
#         r.pause_threshold=1.0
#         r.phrase_threshold=0.3
#         r.sample_rate = 48000
#         r.dynamic_energy_threshold=True
#         r.operation_timeout=5
#         r.non_speaking_duration=0.5
#         r.dynamic_energy_adjustment=2
#         r.energy_threshold=4000
#         r.phrase_time_limit = 10
#         # print(sr.Microphone.list_microphone_names())
#         audio = r.listen(source)
#     try:
#         print("\r" ,end="", flush=True)
#         print("Recognizing......", end="", flush=True)
#         query = r.recognize_google(audio, language='en-in')
#         print("\r" ,end="", flush=True)
#         print(f"User said : {query}\n")
#     except Exception as e:
#         print("Say that again please")
#         return "None"
#     return query

# def cal_day():
#     day = datetime.datetime.today().weekday() + 1
#     day_dict={
#         1:"Monday",
#         2:"Tuesday",
#         3:"Wednesday",
#         4:"Thursday",
#         5:"Friday",
#         6:"Saturday",
#         7:"Sunday"
#     }
#     if day in day_dict.keys():
#         day_of_week = day_dict[day]
#         print(day_of_week)
#     return day_of_week

# def wishMe():
#     hour = int(datetime.datetime.now().hour)
#     t = time.strftime("%I:%M:%p")
#     day = cal_day()

#     if(hour>=0) and (hour<=12) and ('AM' in t):
#         speak(f"Good morning Boss, it's {day} and the time is {t}")
#     elif(hour>=12)  and (hour<=16) and ('PM' in t):
#         speak(f"Good afternoon Boss, it's {day} and the time is {t}")
#     else:
#         speak(f"Good evening Boss, it's {day} and the time is {t}")

# def social_media(command):
#     if 'facebook' in command:
#         speak("opening your facebook")
#         webbrowser.open("https://www.facebook.com/")
#     elif 'whatsapp' in command:
#         speak("opening your whatsapp")
#         webbrowser.open("https://web.whatsapp.com/")
#     elif 'discord' in command:
#         speak("opening your discord server")
#         webbrowser.open("https://discord.com/")
#     elif 'instagram' in command:
#         speak("opening your instagram")
#         webbrowser.open("https://www.instagram.com/")
#     elif 'github' in command:
#         speak("opening your github")
#         webbrowser.open("htttps://www.github.com/")
#     else:
#         speak("No result found")

# def schedule():
#     day = cal_day().lower()
#     speak("Boss today's schedule is ")
#     week={
#     "monday": "Boss, from 9:00 to 10:30 you have Algorithms class, from 10:00 to 11:50 you have System Design class, from 12:00 to 2:00 you have a break, and today you have Programming Lab from 2:00 onwards.",
#     "tuesday": "Boss, from 9:00 to 9:50 you have Web Development class, from 10:00 to 10:50 you have a break, from 11:00 to 12:50 you have Database Systems class, from 1:00 to 2:00 you have a break, and today you have Open Source Projects lab from 2:00 onwards.",
#     "wednesday": "Boss, today you have a full day of classes. From 9:00 to 10:50 you have Machine Learning class, from 11:00 to 11:50 you have Operating Systems class, from 12:00 to 12:50 you have Ethics in Technology class, from 1:00 to 2:00 you have a break, and today you have Software Engineering workshop from 2:00 onwards.",
#     "thursday": "Boss, today you have a full day of classes. From 9:00 to 10:50 you have Computer Networks class, from 11:00 to 12:50 you have Cloud Computing class, from 1:00 to 2:00 you have a break, and today you have Cybersecurity lab from 2:00 onwards.",
#     "friday": "Boss, today you have a full day of classes. From 9:00 to 9:50 you have Artificial Intelligence class, from 10:00 to 10:50 you have Advanced Programming class, from 11:00 to 12:50 you have UI/UX Design class, from 1:00 to 2:00 you have a break, and today you have Capstone Project work from 2:00 onwards.",
#     "saturday": "Boss, today you have a more relaxed day. From 9:00 to 11:50 you have team meetings for your Capstone Project, from 12:00 to 12:50 you have Innovation and Entrepreneurship class, from 1:00 to 2:00 you have a break, and today you have extra time to work on personal development and coding practice from 2:00 onwards.",
#     "sunday": "Boss, today is a holiday, but keep an eye on upcoming deadlines and use this time to catch up on any reading or project work."
#     }
#     if day in week.keys():
#         speak(week[day])

# def openApp(command):
#     if "calculator" in command:
#         speak("opening calculator")
#         os.startfile('C:\\Windows\\System32\\calc.exe')
#     elif "notepad" in command:
#         speak("opening notepad")
#         os.startfile('C:\\Windows\\System32\\notepad.exe')
#     elif "paint" in command:
#         speak("opening paint")
#         os.startfile('C:\\Windows\\System32\\mspaint.exe')

# def closeApp(command):
#     if "calculator" in command:
#         speak("closing calculator")
#         os.system("taskkill /f /im calc.exe")
#     elif "notepad" in command:
#         speak("closing notepad")
#         os.system('taskkill /f /im notepad.exe')
#     elif "paint" in command:
#         speak("closing paint")
#         os.system('taskkill /f /im mspaint.exe')

# def browsing(query):
#     if 'google' in query:
#         speak("Boss, what should i search on google..")
#         s = command().lower()
#         webbrowser.open(f"{s}")
#     # elif 'edge' in query:
#     #     speak("opening your microsoft edge")
#     #     os.startfile()

# def condition():
#     usage = str(psutil.cpu_percent())
#     speak(f"CPU is at {usage} percentage")
#     battery = psutil.sensors_battery()
#     percentage = battery.percent
#     speak(f"Boss our system have {percentage} percentage battery")

#     if percentage>=80:
#         speak("Boss we could have enough charging to continue our recording")
#     elif percentage>=40 and percentage<=75:
#         speak("Boss we should connect our system to charging point to charge our battery")
#     else:
#         speak("Boss we have very low power, please connect to charging otherwise recording should be off...")

# def load_contacts():
#     try:
#         with open("contacts.json", "r") as file:
#             contacts = json.load(file)
#         return contacts["contacts"]
#     except Exception as e:
#         print(f"Error loading contacts: {e}")
#         return {}




# def call_via_whatsapp_desktop(name):
#     contacts = load_contacts()
#     if name in contacts:
#         speak(f"Calling {name} on WhatsApp")
#         # Open WhatsApp desktop app
#         os.startfile("C:\\Users\\user\\Downloads\\WhatsApp Installer.exe")  # Update path as per your setup
#         time.sleep(5)
#         time.sleep(5)
#         pyautogui.click(x=245, y=564)
#         time.sleep(5)
#         time.sleep(5)  # Wait for WhatsApp to open
        
#         # Search for contact
#         pyautogui.hotkey('ctrl', 'f')  # WhatsApp uses Ctrl+F for search
#         pyautogui.write(name)  # Type the contact name
#         pyautogui.click(x = 6 , y = 1006)  # Select the contact
#         time.sleep(1)
        
#         # Initiate call (this step depends on screen layout and may vary)
#         pyautogui.click(x=4, y=218)  # Replace x, y with the call button's location
#     else:
#         speak("Contact not found.")


# if __name__ == "__main__":
#     wishMe()
#     # engine_talk("Allow me to introduce myself I am Groot, the virtual artificial intelligence and I'm here to assist you with a variety of tasks as best I can, 24 hours a day seven days a week.")
#     while True:
#         query = command().lower()
#         # query  = input("Enter your command-> ")
#         if ('facebook' in query) or ('discord' in query) or ('whatsapp' in query) or ('instagram' in query):
#             social_media(query)
#         elif ("university time table" in query) or ("schedule" in query):
#             schedule()
#         elif ("volume up" in query) or ("increase volume" in query):
#             pyautogui.press("volumeup")
#             speak("Volume increased")
#         elif ("volume down" in query) or ("decrease volume" in query):
#             pyautogui.press("volumedown")
#             speak("Volume decrease")
#         elif ("volume mute" in query) or ("mute the sound" in query):
#             pyautogui.press("volumemute")
#             speak("Volume muted")
#         elif ("open calculator" in query) or ("open notepad" in query) or ("open paint" in query):
#             openApp(query)
#         elif ("close calculator" in query) or ("close notepad" in query) or ("close paint" in query):
#             closeApp(query)
#         elif ("what" in query) or ("who" in query) or ("how" in query) or ("hi" in query) or ("thanks" in query) or ("hello" in query):
#                 padded_sequences = pad_sequences(tokenizer.texts_to_sequences([query]), maxlen=20, truncating='post')
#                 result = model.predict(padded_sequences)
#                 tag = label_encoder.inverse_transform([np.argmax(result)])

#                 for i in data['intents']:
#                     if i['tag'] == tag:
#                         speak(np.random.choice(i['responses']))
#         elif ("open google" in query) or ("open edge" in query):
#             browsing(query)
#         elif ("system condition" in query) or ("condition of the system" in query):
#             speak("checking the system condition")
#             condition()
#         elif ("call" in query):
#             speak('Calling...')
#             call_via_whatsapp_desktop("Siva Rama Raju")
#         elif "exit" in query:
#             sys.exit()
# speak("I AM GROOOT....")


import datetime
import os
import sys
import time
import webbrowser
import pyautogui
import pyttsx3
import speech_recognition as sr
import json
import pickle
import random
import numpy as np
import psutil
import subprocess
import requests
import pyjokes
from time import sleep
from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM


# Load the DialoGPT model
model_name = "meta-llama/Llama-2-7b-hf"
tokenizer = AutoTokenizer.from_pretrained(model_name , use_fast = False)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Initialize the text generation pipeline
chat_pipeline = pipeline('text-generation', model=model, tokenizer=tokenizer)

def initialize_engine():
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 160)
    engine.setProperty('volume', 1.0)
    return engine

def speak(text):
    engine = initialize_engine()
    engine.say(text)
    engine.runAndWait()

def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=0.5)
        print("Listening.......", end="", flush=True)
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=8)
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}")
            print('command function succeded')
        except Exception as e:
            print(e)
            speak("Sorry, I didn't catch that. Can you say it again?")
            return "None"
    return query.lower()

def cal_day():
    day_dict = {
        1: "Monday", 2: "Tuesday", 3: "Wednesday", 
        4: "Thursday", 5: "Friday", 6: "Saturday", 7: "Sunday"
    }
    day = datetime.datetime.today().weekday() + 1
    return day_dict.get(day, "Unknown")

def wishMe():
    hour = int(datetime.datetime.now().hour)
    day = cal_day()
    time_now = time.strftime("%I:%M %p")
    greeting = (
        "Good Morning Boss" if hour < 12 else
        "Good Afternoon Boss" if 12 <= hour < 18 else
        "Good Evening Boss"
    )
    speak(f"{greeting} Boss! It's {day}, and the time is {time_now}. How can I assist you?")

def weather():
    API_KEY = "dfb7f285b50581d2ef648cdd7bde31d0"
    CITY = "Bhimavaram"
    URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"
    try:
        response = requests.get(URL)
        data = response.json()
        if data["cod"] != "404":
            weather_desc = data["weather"][0]["description"]
            temp = data["main"]["temp"]
            speak(f"The current weather in {CITY} is {weather_desc} with a temperature of {temp}°C.")
        else:
            speak("Sorry, I couldn't fetch the weather details.")
    except Exception as e:
        speak("Unable to fetch weather information right now.")

def play_music():
    speak("What song should I play?")
    song = command()
    if song != "None":
        webbrowser.open(f"https://www.youtube.com/results?search_query={song}")
        speak(f"Playing {song} on YouTube.")

def tell_joke():
    joke = pyjokes.get_joke()
    speak(joke)

def play_game():
    speak("Let's play a guessing game. I'm thinking of a number between 1 and 100. Can you guess it?")
    number = random.randint(1, 100)
    attempts = 0
    while True:
        guess = command()
        if guess.isdigit():
            guess = int(guess)
            attempts += 1
            if guess < number:
                speak("Too low! Try again.")
            elif guess > number:
                speak("Too high! Try again.")
            else:
                speak(f"Congratulations! You guessed the number {number} in {attempts} attempts.")
                break
        else:
            speak("Please say a number.")

def advanced_chat(user_query):
    conversation = chat_pipeline(user_query , max_new_tokens=500, do_sample=True)
    response = conversation[0]['generated_text']
    speak(response)

if __name__ == "__main__":
    wishMe()
    speak('I am Grooot!!!!')
    while True:
        query = command()

        if "weather" in query:
            weather()
        elif "play song" in query or "play music" in query:
            play_music()
        elif "joke" in query:
            tell_joke()
        elif "game" in query:
            play_game()
        elif "exit" in query or "bye" in query:
            speak("Goodbye! Have a nice day.")
            break
        elif query != "None":
            speak("Let me process that.")
            advanced_chat(query)
