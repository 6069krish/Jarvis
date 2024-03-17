import re
import pyttsx3
import speech_recognition as sr
import webbrowser
import wolframalpha
import datetime 
import os
import wikipedia
import pyautogui
import winsound
import pyjokes
import subprocess
chatbot_script = 'chatbot.py'

input('')
def takeCommand():
    r = sr.Recognizer() 

    with sr.Microphone() as source:
        print("Listening.....")
        winsound.Beep(500 , 600)
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        

    try:
     print("Recognizing....")

     winsound.Beep(300 , 400)
     query = r.recognize_google(audio, language='en-in')
     print(f"user said: {query}\n")

    
    except Exception as e:
      print("say that again please" , str(e))
      speak("say that again please")
      return " "
    return query

engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices') 
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio) 
    engine.runAndWait()

def handle_query_with_chatbot(user_query):
    # Call the chatbot script and pass the user query as an argument
    result = subprocess.run(['python', chatbot_script, user_query], capture_output=True, text=True)
    # Return the chatbot's response
    return result.stdout.strip()

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

        client = wolframalpha.Client("7G6TQL-KK3HPEY2UA")
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
            webbrowser.open(f"{domain}.com")

        



if __name__ == "__main__":
        
        
        while True:
            input('')
            query = takeCommand().lower()
            script_to_run = 'chatbot.py'
            try:
                if "" in query:
                    subprocess.run(['python', script_to_run])

            except:
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


                elif "open" in query:
                    web()
           

                elif "time" in query:
                    time()
            
        
                elif "why"in query or "what"in query or 'who'in query or 'when' in query or 'how' in query or 'where' in query:
                    wolfrmalpha()
            
                else:
                    print('error404')
