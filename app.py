from flask import Flask, render_template, request, jsonify
import pandas as pd
import joblib

app = Flask(__name__)

# Saved model aur processor load karo
model = joblib.load('model.pkl')
processor = joblib.load('processor.pkl')


@app.route('/')
def home():
     return render_template('index.html') 


@app.route('/predict', methods=['POST'])
def predict():

    data = request.get_json()

    new_car = pd.DataFrame({
        'AccelSec': [data['AccelSec']],
        'TopSpeed_KmH': [data['TopSpeed_KmH']],
        'Range_Km': [data['Range_Km']],
        'Efficiency_WhKm': [data['Efficiency_WhKm']],
        'FastCharge_KmH': [data['FastCharge_KmH']],
        'RapidCharge': [data['RapidCharge']],
        'PowerTrain': [data['PowerTrain']],
        'PlugType': [data['PlugType']],
        'BodyStyle': [data['BodyStyle']],
        'Segment': [data['Segment']],
        'Seats': [data['Seats']]
    })

    # Same preprocessing
    new_car_processed = processor.transform(new_car)

    # Prediction
    prediction = model.predict(new_car_processed)

    return jsonify({
        'predicted_price': round(float(prediction[0]), 2)
    })


if __name__ == '__main__':
    app.run(debug=True)