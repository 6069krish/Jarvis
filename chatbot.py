
import json
import os
from difflib import get_close_matches
import pyttsx3
import speech_recognition as sr
import pyttsx3
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
import pyttsx3
import speech_recognition as sr
from jarvis import *

engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices') 
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio) 
    engine.runAndWait()

def load_knowledge_base(file_path: str) -> dict:
    with open(file_path , 'r') as file:
        data: dict = json.load(file)
        return data

def save_knowledge_base(file_path : str , data:dict) :
    with open(file_path , 'w') as file:
        json.dump(data , file ,indent=2)

def find_best_match(user_question: str , questions: list[str]) -> str | None:
    matches: list = get_close_matches(user_question, questions, n=1 ,cutoff=0.6)
    return matches[0] if matches else None 

def get_answer_for_question(question: str , knowledge_base: dict) -> str | None:
    for q in knowledge_base["questions"]:
        if q["question"] == question:
            return q["answer"]
        
def chat_bot():
    knowledge_base: dict  = load_knowledge_base('intents.json')
    engine = pyttsx3.init()

    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    while True:
        with microphone as source:
            print('Listening...')
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

        try:
            print('Recognizing...')
            query = recognizer.recognize_google(audio)
            print(f'You said: {query}')

            if query.lower() == 'quit':
                break

            best_match = find_best_match(query, [q["question"] for q in knowledge_base["questions"]])

            if best_match:
                answer = get_answer_for_question(best_match, knowledge_base)
                print(f'Bot: {answer}')
                engine.say(answer)
                engine.runAndWait()
            else:
                print("Bot: I don't know. Please teach me.")
                speak("Bot: I don't know. Please teach me.")
                new_answer = input('Type the answer or "skip" to skip: ')

                if new_answer.lower() != 'skip':
                    knowledge_base["questions"].append({"question": query, "answer": new_answer})
                    save_knowledge_base('intents.json', knowledge_base)
                    print('Bot: Thank you, I have learned.')
                    engine.say('Thank you, I have learned.')
                    engine.runAndWait()

        except sr.UnknownValueError:
            print("Sorry, I could not understand what you said.")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service: {e}")

if __name__ == '__main__' :
    query = takeCommand()
    while True:
        if "stop" not in query:
            chat_bot()

        else:
            if "stop" in query:
                subprocess.run(['python' , 'jarvis.py'])
