import numpy as np
import pandas as pd
from keras.models import load_model
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    frenchtext = request.form['frenchtext']
    return frenchtext

if __name__ == '__main__':
    app.run()