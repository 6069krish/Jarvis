import random
import json
import pickle
import numpy as np
import nltk
from nltk.stem import WordNetLemmatizer
import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
import pyttsx3
import speech_recognition as sr
import subprocess
from keras.models import load_model

lemmatizer = WordNetLemmatizer()

engine = pyttsx3.init()

with open('intents.json') as json_data:
    intents = json.load(json_data)

words = pickle.load(open('words.pkl', 'rb'))
classes = pickle.load(open('classes.pkl', 'rb'))

model = load_model('chatbot_model.h5')
engine = pyttsx3.init()
recognizer = sr.Recognizer()

def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word) for word in sentence_words]
    return sentence_words

def bag_of_words(sentence):
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)
    for w in sentence_words:
        for i, word in enumerate(words):
            if word == w:
                bag[i] = 1 
    return np.array(bag)

def predict_class(sentence):
    bow = bag_of_words(sentence)
    res = model.predict(np.array([bow]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({'intent': classes[r[0]], 'probability': str(r[1])})
    return return_list

def get_response(intents_list, intents_json):
    tag = intents_list[0]['intent']
    list_of_intents = intents_json['intents']
    for intent in list_of_intents:
        if intent['tag'] == tag:
            responses = intent['responses']
            result = random.choice(responses)
            break
    else:
        result = "I'm sorry, I don't understand."
    return result

print("GO! BOT IS RUNNING MOTHERFUCKER")

while True:
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        user_input = recognizer.recognize_google(audio)
        print("User input:", user_input)
        ints = predict_class(user_input)
        res = get_response(ints, intents)
        print("Bot response:", res)
        engine.say(res)
        engine.runAndWait()

    except:
        script_to_run = 'jarvis.py'
        subprocess.run(['python', script_to_run])


