from flask import Flask, request, jsonify
import joblib
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load the saved model and encoder
model = joblib.load('disease_prediction_model.pkl')
le_disease = joblib.load('label_encoder.pkl')

@app.route('/')
def home():
    return "Disease Prediction API is running!"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    # Example: data = {"symptoms": ["fever", "cough", "headache"]}
    symptoms = data.get("symptoms", [])

    # Convert symptoms to one-hot encoded vector (as done in your training dataset)
    # Example: your training dataset columns except disease
    all_symptoms = ['fever', 'cough', 'headache', 'fatigue', 'nausea']  # Replace with your actual symptom columns

    input_data = [1 if s in symptoms else 0 for s in all_symptoms]
    input_df = pd.DataFrame([input_data], columns=all_symptoms)

    # Predict disease
    y_pred = model.predict(input_df)
    disease = le_disease.inverse_transform(y_pred)[0]

    return jsonify({
        "predicted_disease": disease
    })

if __name__ == '__main__':
    app.run(debug=True)
