from flask import Flask, render_template, request
import numpy as np
import joblib


app = Flask(__name__)

model = joblib.load('Crop_recommendation.sav')

Crops = ['rice', 'maize', 'chickpea', 'kidneybeans', 'pigeonpeas',
       'mothbeans', 'mungbean', 'blackgram', 'lentil', 'pomegranate',
       'banana', 'mango', 'grapes', 'watermelon', 'muskmelon', 'apple',
       'orange', 'papaya', 'coconut', 'cotton', 'jute', 'coffee']

sc_mean = np.array([ 50.39261364,  52.88238636,  47.23579545,  25.58610532,
        71.20236431,   6.46069391, 104.99553826])
sc_std = np.array([36.6511325 , 32.50093228, 49.19601994,  5.08611542, 22.50626072,
        0.78173883, 55.66283749])


def scale(x):
    sc = (x-sc_mean)/sc_std
    sc = np.array(sc)
    return sc


       
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def result():
    N = float(request.form['N'])
    P = float(request.form['P'])
    K = float(request.form['K'])
    T = float(request.form['T'])
    H = float(request.form['H'])
    PH = float(request.form['PH'])
    R = float(request.form['R'])

    arr = np.array([[N,P,K,T,H,PH,R]])
    arr = scale(arr)
    ind = model.predict(arr)
    pred = np.argmax(ind)
    print(pred)    
    return render_template('result.html', result=Crops[pred])



if __name__ == '__main__':
    app.run()