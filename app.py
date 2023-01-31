import os
from flask import Flask, render_template, request
import pickle
import numpy as np

import tensorflow as tf

app = Flask(__name__)

def predict(values, dic):
    
    
    

    #
    if len(values) == 13:
        model = pickle.load(open('models/heart.pkl','rb'))
        values = np.asarray(values)
        return model.predict(values.reshape(1, -1))[0]

    
@app.route("/")
def home():
    return render_template('home.html')



@app.route("/heart", methods=['GET', 'POST'])
def heartPage():
    return render_template('heart.html')


@app.route("/predict", methods = ['POST', 'GET'])
def predictPage():
    try:
        if request.method == 'POST':
            to_predict_dict = request.form.to_dict()

            for key, value in to_predict_dict.items():
                try:
                    to_predict_dict[key] = int(value)
                except ValueError:
                    to_predict_dict[key] = float(value)

            to_predict_list = list(map(float, list(to_predict_dict.values())))
            pred = predict(to_predict_list, to_predict_dict)
    except:
        message = "Please enter valid data"
        return render_template("home.html", message=message)

    return render_template('predict.html', pred=pred)



if __name__ == '__main__':
    app.run(debug = True)