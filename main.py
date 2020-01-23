import string
import numpy as np
import pandas as pd
from keras.models import load_model
from keras.preprocessing.text import Tokenizer
from flask import Flask, request, render_template
from keras.preprocessing.sequence import pad_sequences

max_len_eng = 8
max_len_fre = 14

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    french = np.array([request.form['frenchtext']])
    french = preprocessing_input_text(french)
    model = load_model('model/weights-improvement.hdf5')
    prediction = model.predict_classes(french.reshape(french.shape[0], french.shape[1]))
    text = predict_text(prediction)[0]
    return text

def predict_text(prediction):
    preds_text = []
    for i in prediction:
        temp = []
        for j in range(len(i)):
            t = get_word(i[j], english_tokenizer)
            if j > 0:
                if (t == get_word(i[j-1], english_tokenizer)) or (t == None):
                    temp.append('')
                else:
                    temp.append(t)
            else:
                if(t == None):
                    temp.append('')
                else:
                    temp.append(t)
        preds_text.append(' '.join(temp))
    return preds_text

def get_word(n, tokenizer):
    for word, index in tokenizer.word_index.items():
        if index == n:
            return word
    return None

def tokenizer(corpus):
    tokenizer = Tokenizer()
    tokenizer.fit_on_texts(corpus)
    return tokenizer

def encode_sequences(tokenizer, length, text):
    sequences = tokenizer.texts_to_sequences(text)
    sequences = pad_sequences(sequences, maxlen=length, padding='post')
    return sequences

def create_tokenizer():
    data = pd.read_csv('https://github.com/amarlearning/neural-machine-translation/raw/master/dataset/fra-eng/fra.tsv', delimiter='\t')
    data = data.iloc[:55000, :]
    english = data.english.values
    french = data.french.values
    english = [s.translate(str.maketrans('', '', string.punctuation)) for s in english]
    french = [s.translate(str.maketrans('', '', string.punctuation)) for s in french]
    english = [s.lower() if isinstance(s, str) else s for s in english]
    french = [s.lower() if isinstance(s, str) else s for s in french]
    english_tok = tokenizer(english)
    french_tok = tokenizer(french)
    print("tokenizer done")
    return (french_tok, english_tok)


def preprocessing_input_text(french):
    french = [s.translate(str.maketrans('', '', string.punctuation)) for s in french]
    french = [s.lower() if isinstance(s, str) else s for s in french]
    french = encode_sequences(french_tokenizer, max_len_fre, french)
    return french

french_tokenizer, english_tokenizer = create_tokenizer()

if __name__ == '__main__':
    app.run()