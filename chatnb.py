from keras.preprocessing.text import Tokenizer, text_to_word_sequence
from keras.preprocessing.sequence import pad_sequences
import sys, os, re, csv, codecs, numpy as np, pandas as pd
from keras.models import model_from_json
from keras.preprocessing.sequence import pad_sequences
from keras.backend import argmax
import tensorflow as tf
import pickle

filename= "tokenizer.sav"

json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
# load weights into new model
loaded_model.load_weights("model.h5")
print("Loaded model from disk")

loaded_model.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy'])

# print("Hiii THis is a CHat App, Cusss and show Me BItch !!!!!")
tokenizer = pickle.load(open(filename, 'rb'))

def preprocess(comment):
	# words = text_to_word_sequence(comment,filters='!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~\t\n',lower=True,split=" ")
	max_features = 20000
	# tokenizer = Tokenizer(num_words=max_features)
	# tokenizer.fit_on_texts(list(comment))
	tokenizer = pickle.load(open(filename, 'rb'))
	list_tokenized_train = tokenizer.texts_to_sequences([comment])
	maxlen = 200
	X_t = pad_sequences(list_tokenized_train, maxlen=maxlen)
	# print(X_t)
	y_pred = loaded_model.predict(X_t)
	return np.max(y_pred)*100


while True:
	comment=raw_input("---->")
	if(comment == "exit"):
		break
	tokenizer = preprocess(comment)
	if(tokenizer>=95):
		print("You have a dirty mouth Sir")
	if(tokenizer>=69 and tokenizer<95):
		print("We want you to be good to others")