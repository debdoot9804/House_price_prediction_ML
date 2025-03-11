import pickle
from flask import Flask,request,render_template
import pandas as pd
import numpy as np

# Initialize Flask app
app = Flask(__name__)

scaler=pickle.load(open('scaler.pkl','rb')) #Loading scaler
model=pickle.load(open('xgb_model.pkl','rb'))# Loading model

@app.route('/')

def index():
    return render_template('index.html')

 
@app.route('/predict', methods=['GET','POST'])
def predict():
    if request.method=="POST":
        Latitude=float(request.form.get('Latitude'))
        Housing_Median_Age =float(request.form.get('Housing Median Age'))
        Total_Rooms=float(request.form.get('Total Rooms'))
        Households=float(request.form.get('Households'))
        Median_Income=float(request.form.get('Median Income'))
        ocean_proximity_INLAND=float(request.form.get('ocean_proximity_INLAND'))
        ocean_proximity_NEAR_BAY=float(request.form.get('ocean_proximity_NEAR BAY'))
        ocean_proximity_NEAR_OCEAN=float(request.form.get('ocean_proximity_NEAR OCEAN'))

        data_scaled=scaler.transform([[Latitude,Housing_Median_Age,Total_Rooms,Households,Median_Income,ocean_proximity_INLAND,ocean_proximity_NEAR_BAY,ocean_proximity_NEAR_OCEAN]])
        result=model.predict(data_scaled)

        
        return render_template('home.html',results=result[0])


    else:

        return render_template('home.html')
        
if __name__=="__main__":
     app.run(host="0.0.0.0")

    
#  if __name__ == '__main__':
#     app.run(debug=True)