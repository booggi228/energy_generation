from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np

# Define a flask app
app = Flask(__name__)

# Load trained model
model = pickle.load(open('forest.pickle', 'rb'))

# Main page
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')

# Get the information from post request
@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        power=float(request.form['power'])
        station=request.form['station']
        if(station=='ВЕС'):
            station=1
        elif(station=='СЕС'):
            station=2
        elif(station=='мГЕС'):
            station=3
        else:
            station=4
        substation=request.form['substation']
        if(substation=='Біогаз'):
            substation=1
        elif(substation=='Біомаса'):
            substation=2
        if(substation=='Дах'):
            substation=3
        elif(substation=='Земля'):
            substation=4
        if(substation=='Мала'):
            substation=5
        elif(substation=='Мікро'):
            substation=6
        if(substation=='Міні'):
            substation=7
        else:
            substation=0	
        obl=request.form['obl']
        if obl == 'Волинська':
            obl = 1
        elif obl == 'Вінницька':
            obl = 2
        elif obl == 'Дніпропетровська':
            obl = 3
        elif obl == 'Донецька':
            obl = 4
        elif obl == 'Житомирська':
            obl = 5
        elif obl == 'Закарпатська':
            obl = 6
        elif obl == 'Запорізька':
            obl = 7
        elif obl == 'Київська':
            obl = 8
        elif obl == 'Кіровоградська':
            obl = 9
        elif obl == 'Луганська':
            obl = 10
        elif obl == 'Львівська':
            obl = 11
        elif obl == 'Миколаївська':
            obl = 12
        elif obl == 'Одеська':
            obl = 13
        elif obl == 'Полтавська':
            obl = 14
        elif obl == 'Рівненська':
            obl = 15
        elif obl == 'Сумська':
            obl = 16
        elif obl == 'Тернопільська':
            obl = 17
        elif obl == 'Харківська':
            obl = 18
        elif obl == 'Херсонська':
            obl = 19
        elif obl == 'Хмельницька':
            obl = 20
        elif obl == 'Черкаська':
            obl = 21
        elif obl == 'Чернівецька':
            obl = 22
        elif obl == 'Чернігівська':
            obl = 23
        elif obl == 'м.Київ':
            obl = 24
        else:
            obl = 0

        # Make prediction
        prediction=model.predict([[station, substation, obl, power]])
        output=round(prediction[0],2)
        
        return render_template('index.html',prediction_text="Планове вироблення електроенергії за рік {} МВт.".format(output))
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)

