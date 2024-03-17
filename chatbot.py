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
from jarvis import *
r= sr.Recognizer()
lemmatizer = WordNetLemmatizer()

engine = pyttsx3.init()
with open('intents.json') as json_data:
    intents = json.load(json_data)

words = pickle.load(open('words.pkl', 'rb'))
classes = pickle.load(open('classes.pkl', 'rb'))

# Load the trained model
model = load_model('chatbot_model.h5')

def clean_up_sentence(sentence):
    # Tokenize and lemmatize the sentence
    return [lemmatizer.lemmatize(word.lower()) for word in nltk.word_tokenize(sentence)]

def bag_of_words(sentence):
    # Create a bag of words representation for the sentence
    bag = [0] * len(words)
    sentence_words = clean_up_sentence(sentence)
    for w in sentence_words:
        if w in words:
            bag[words.index(w)] = 1
    return np.array(bag)

def predict_class(sentence):
    # Predict the class of the sentence
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

def process_query(user_query):
    # Process user's query and return response
    ints = predict_class(user_query)
    res = get_response(ints, intents)
    return res

def get_chatbot_response(user_input):
    # Get response from chatbot
    ints = predict_class(user_input)
    res = get_response(ints, intents)
    return res

print("GO! BOT IS RUNNING MOTHERFUCKER")

while True:
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    # try:
        user_input = r.recognize_google(audio)
        print("User input:", user_input)
        ints = predict_class(user_input)
        res = get_response(ints, intents)
        print("Bot response:", res)
        chatbot_response = get_chatbot_response(user_input)
    # if chatbot_response == "I'm sorry, I don't understand.":
    #     subprocess.run(['python', 'jarvis.py'])
    # else:
    #     engine.say(chatbot_response)
    #     engine.runAndWait()

    # except:
    #     script_to_run = 'jarvis.py'
    #     subprocess.run(['python', script_to_run])


