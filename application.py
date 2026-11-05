from flask import Flask , request, jsonify, render_template
import pickle 
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
application = Flask(__name__)
app= application
ridge_model = pickle.load(open('models/ridge.pkl', 'rb'))

standard_scaler = pickle.load(open('models/scaler.pkl', 'rb'))
@app.route("/")
def index():
    return render_template('index.html')


@app.route("/predict_data", methods=['GET', 'POST'])
def predict_data():
    if request.method == 'POST':
        Temperature = float(request.form.get('Temperature'))
        RH = float(request.form.get('RH'))
        Ws = float(request.form.get('Ws'))
        Rain = float(request.form.get('Rain'))
        FFMC = float(request.form.get('FFMC'))
        DMC = float(request.form.get('DMC'))
        ISI = float(request.form.get('ISI'))
        Classes = float(request.form.get('Classes'))
        region = float(request.form.get('region'))

        new_data_scaled=standard_scaler.transform([[Temperature, RH, Ws, Rain, FFMC, DMC, ISI, Classes, region]])
        result = ridge_model.predict(new_data_scaled)
        fwi = result[0]
        if fwi >= 20:
            fire_status = "Yes"
        else:
            fire_status = "No"
        return render_template('home.html',  result=round(float(fwi), 2), fire_status=fire_status)    
    else:
        return render_template('home.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)