import numpy as np
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()

import json
import pickle
import random 

import nltk
# nltk.download('wordnet')
# nltk.download('punkt')
from nltk.stem import WordNetLemmatizer
import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

from keras.models import Sequential
from keras.layers import Dense , Activation , Dropout 
from keras.optimizers import SGD

lemmatizer = WordNetLemmatizer()

with open('intents.json') as json_data:
    intents = json.load(json_data)


words = []
classes = []
documents = []
ignore_words = ['?']

for intent in intents['intents']:
    for pattern in intent['patterns']:
        word_list = nltk.word_tokenize(pattern)
        words.extend(word_list)
        documents.append((word_list , intent['tag']))
    if intent['tag'] not in classes:
        classes.append(intent['tag'])


words = [stemmer.stem(word_list.lower()) for word_list in words if word_list not in ignore_words]
words = sorted(list(set(words)))
classes = sorted(set(classes))
pickle.dump(words , open ("words.pkl ", 'wb'))
pickle.dump(classes , open ("classes.pkl ", 'wb'))

# Initialize training data and output
training_data = []
output_empty = [0] * len(classes)

for document in documents:
    bag = []
    word_patterns = document[0]
    word_patterns = [lemmatizer.lemmatize(word.lower()) for word in word_patterns]
    for word in words:
        bag.append(1) if word in word_patterns else bag.append(0)
    output_row = list(output_empty)
    output_row[classes.index(document[1])] = 1
    training_data.append(bag + output_row) 

random.shuffle(training_data)
training_data = np.array(training_data)
train_x = training_data[:, :len(words)]
train_y = training_data[:, len(words):]
model = Sequential()
model.add(Dense(128, input_shape=(len(train_x[0]),), activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(len(train_y[0]), activation='softmax')) 
sgd = SGD(learning_rate=0.01 , decay =1e-6,momentum=0.9 , nesterov=True)
model.compile(loss='categorical_crossentropy' , optimizer = sgd,metrics=['accuracy'])
hist = model.fit(train_x, train_y, epochs=200, batch_size=5, verbose=1) 
model.save('chatbot_model.h5', hist)
print('done')