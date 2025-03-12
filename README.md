
# House Price Prediction - Machine Learning Project

## 📌 Project Overview
This project is a **House Price Prediction** model using **XGBoost Regressor**. The model takes various house-related features as input and predicts the house price. The application is deployed using **Flask on Render** and has a **Streamlit front-end** for user interaction.

## 🚀 Features
- **Machine Learning Model**: Trained using XGBoost Regressor
- **Data Scaler**: Uses `StandardScaler` for feature scaling
- **Flask API**: Backend for model inference
- **Postman Integration**: Test the API using JSON input
- **Streamlit UI**: User-friendly front-end interface for predictions
- **Deployment**: Hosted on **Render** and **Streamlit Cloud**

###To Run this project follow the steps ----

## 🛠️ Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/debdoot9804/House_price_prediction_ML.git
   cd House_price_prediction_ML
   ```

2. **Create Virtual Environment & Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run Flask App** (Local Testing)
   ```bash
   python app.py
   ```

4. **Access API on Postman**
   - Use `POST` request to `http://127.0.0.1:5000/predict`
   - Send JSON data with house features

5. **Run Streamlit App** (Frontend)
   ```bash
   streamlit run app.py
   ```

## 🎯 Usage
### 🔹 Using Postman (API Testing)
- **URL**: `https://flask-api-house-price-prediction.onrender.com/`
- **Method**: `POST`
- **JSON Input Example**:
  ```json
      {
    "latitude": 61.33,
    "housing_median_age": 28.0,
    "total_rooms": 719.0,
    "households": 111.0,
    "median_income": 11.5252,
    "ocean_proximity_INLAND": 1,
    "ocean_proximity_NEAR BAY": 0,
    "ocean_proximity_NEAR OCEAN": 0

  }
  ```
- **Response Example**:
  ```json
  {
    "House Price Prediction": 311946.28125
  }
  ```

### 🔹 Using Streamlit (Web UI)
1. Open `https://housepricepredictionml-cdg4hdgdcxcfsucmipvfwh.streamlit.app/`
2. Enter feature values in the form
3. Click **Predict** to get the house price

## 🌍 Deployment Details
- **Flask Backend**: Hosted on **Render**
- **Streamlit Frontend**: Hosted on **Streamlit Cloud**
- **GitHub Repo**: [House Price Prediction ML](https://github.com/debdoot9804/House_price_prediction_ML)

## 📜 Project Structure
```
House_price_prediction_ML/
│── app.py                # Flask App
│── stream_app.py      # Streamlit Frontend
│── xgb_model.pkl         # Model pickle file
│── requirements.txt      # Dependencies
│── Procfile              # Deployment Config for Render
│── README.md             # Project Documentation
```




---
📢 **Author**: [Debdoot9804](https://github.com/debdoot9804)  
🔗 **Project Repo**: [GitHub](https://github.com/debdoot9804/House_price_prediction_ML)

