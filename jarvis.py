import re
import pyttsx3
import speech_recognition as sr
import webbrowser
import wolframalpha
import datetime 
import os
import datetime
import wikipedia
import pyautogui
import winsound
import subprocess
import pyjokes
os.environ.get('GOOGLE_APPLICATION_CREDENTIALS') 
input('')
def takeCommand():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening.....")
        winsound.Beep(500 , 600)
        recognizer.pause_threshold = 1
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
     print("Recognizing....")

     winsound.Beep(300 , 400)
     query = recognizer.recognize_google(audio, language='en-in')
     print(f"user said: {query}\n")
     

    
    except Exception as e:
      print("say that again please" , str(e))
      speak("say that again please")
      return " "
    return query

    # except sr.UnknownValueError:
    #     print("Sorry, I didn't catch that. Could you please repeat?")
    #     return query  # Return an empty string in case of recognition failure

    # except sr.RequestError as e:
    #     print("Could not request results; {0}".format(e))
    #     return query
    
engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices') 
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio) 
    engine.runAndWait()


def wiki():
    try:
       
        p = wikipedia.page(f"{query}")
        print(wikipedia.summary(query, sentences=2))  
        speak(wikipedia.summary(query, sentences=2))

    except:
        print("Couldnt Get you")
        speak("Couldnt Get you")

def jokes():
    joke = pyjokes.get_joke()
    print(joke)
    speak(joke)


def wolfrmalpha(): 
    try: 

        client = wolframalpha.Client("7your_client_id")
        res = client.query(query)
        output = next(res.results).text
        print(output)
        speak(output)

    except:
        wiki()

def time():

    current_time = datetime.datetime.now()
    time_in_words = current_time.strftime("%I:%M %p")
    print("The time is:", time_in_words)
    # speak("The time is:", time_in_words)

def web():
            
            re.search('open' , query)
            domain = query.split(' ')[-1]
            speak(f'Alright sir !! Opening {domain}')
            webbrowser.open(f"https://{domain}.com")

        



if __name__ == "__main__":
        
        
        while True:
            input('')
            query = takeCommand().lower()
           
            if "joke" in query:
                jokes()   

            elif "stop" in query:
                speak("stopping sir")
                winsound.Beep(700 , 800)
                pyautogui.click(1915, 0)
                # pyautogui.hotkey("ctrl" , "q")
                # pyautogui.click(937,611)

            elif "video" in query:
                os.startfile("C:\\Users\\ghosh\\OneDrive\\Desktop\\SOURISH.mp4")
                pyautogui.click(1293,1058)
                break

            elif 'like'in query and 'eat' in query:
                print('i like to eat data')
                speak('i like to eat data')

            elif "conversation" in query and "talk" in query and "chatbot" in query:
                subprocess.run(["python", "chatbot.py"], capture_output=True, text=True)

            elif "open" in query:
                web()
           

            elif "time" in query:
                 time()
            
        
            elif "why"in query or "what"in query or 'who'in query or 'when' in query or 'how' in query or 'where' in query:
                wolfrmalpha()

