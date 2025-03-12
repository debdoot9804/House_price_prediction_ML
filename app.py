import pickle
from flask import Flask,request,render_template,jsonify
import pandas as pd
import numpy as np

# Initialize Flask app
app = Flask(__name__)

scaler=pickle.load(open('scaler.pkl','rb')) #Loading scaler
model=pickle.load(open('xgb_model.pkl','rb'))# Loading model

@app.route('/',methods=['GET','POST'])

# def index():
#     return render_template('index.html')

#@app.route('/predict', methods=['POST'])
def predict():
    try:
        
        data = request.get_json()
        print("Received JSON Data:", data)  # Check supplied values from Postman
        
        # Ensure all required features exist
        required_features = [
            'latitude', 'housing_median_age', 'total_rooms',
            'households', 'median_income', 'ocean_proximity_INLAND',
            'ocean_proximity_NEAR BAY', 'ocean_proximity_NEAR OCEAN'
        ]

        
        
        # Converting input values to float
        features = np.array([[float(data[feature]) for feature in required_features]])
        
        # Apply scaling
        data_scaled = scaler.transform(features)

        # Make prediction
        prediction = model.predict(data_scaled)[0]

        return jsonify({"House Price Prediction": float(prediction)})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
    
