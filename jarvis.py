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

        client = wolframalpha.Client("your_app_id")
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
            if "who are you" in query:
                print("I am JARVIS your favorite personal voice assistant")
                speak("I am JARVIS your favorite personal voice assistant")


            elif "joke" in query:
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
            elif 'hello' in query or 'hi'in query or 'hey' in query or 'sup' in query or 'heyo'in query or'whatsup' in query:
                print("Hello!")
                speak("Hello!")

            elif 'bye' in query or 'goodbye' in query:
                print("See you!")
                speak("See you!")

            elif 'how are you' in query:
                print("i am doing fine, and you?")
                speak("i am doing fine, and you?")

            elif 'thank' in query or  'thanks' in query:
                print("You're welcome!")
                speak("You're welcome!")

            elif 'your'in query and 'name' in query:
                print('i am jarvis')
                speak('i am jarvis')

            elif 'like'in query and 'eat' in query:
                print('i like to eat data')
                speak('i like to eat data')

            elif 'you'in query and 'bad' in query:
                print('nope i am not')
                speak('nope i am not')

            elif 'fine'in query and 'i' in query:
                print('great')
                speak('great')

            elif 'where'in query and'you' in query:
                print('on internet')
                speak('on internet')
            
            elif 'created'in query and'you' in query:
                print('Ryan And Krishnendu')
                speak('Ryan And Krishnendu')

            
            # elif 'your' in query and 'name' in query:
            #     print("You're welcome!")
            #     speak("You're welcome!")

            # elif 'thank' or  'thanks' in query:
            #     print("You're welcome!")
            #     speak("You're welcome!")

            elif "open" in query:
                web()
           

            elif "time" in query:
                time()
            
        
            elif "why"in query or "what"in query or 'who'in query or 'when' in query or 'how' in query or 'where' in query:
                wolfrmalpha()
            
            elif 'tower' in query:
                speak('activating lights')
            else:
                print('error404')
