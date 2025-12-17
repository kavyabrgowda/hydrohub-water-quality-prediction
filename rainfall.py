import requests
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.impute import SimpleImputer

# OpenWeatherMap API Configuration
API_KEY = "dc3bc59552a81a52e97620cf6ce6e6bc"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

# Load dataset and train model
file_path = "rainfall.csv"
df = pd.read_csv(file_path)

# Handle missing values
df_numeric = df.drop(columns=['DIVISION', 'YEAR'], errors='ignore')
imputer = SimpleImputer(strategy="mean")
df_numeric_imputed = pd.DataFrame(imputer.fit_transform(df_numeric), columns=df_numeric.columns)

# Train Linear Regression model
X = df_numeric_imputed.drop(columns=["ANNUAL"], errors="ignore")
y = df_numeric_imputed["ANNUAL"]
model = LinearRegression()
model.fit(X, y)

def get_weather_data(city):
    """Fetch real-time weather data from OpenWeatherMap."""
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if response.status_code == 200:
        rainfall = data.get("rain", {}).get("1h", None)
        if rainfall is None:
            # If real-time rainfall isn't available, estimate it using humidity
            humidity = data["main"]["humidity"]
            temperature = data["main"]["temp"]

            # Simple estimation: More humidity + moderate temp → More rainfall
            estimated_rainfall = (humidity / 100) * (30 - abs(temperature - 25)) * 0.1
            rainfall = round(estimated_rainfall, 2)  # Convert to a reasonable scale

        return {
            "rainfall": rainfall,
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "weather_description": data["weather"][0]["description"]
        }
    
    return None  # Handle API failure



def get_rainfall_prediction(city):
    """Predict annual rainfall using real-time data."""
    weather = get_weather_data(city)
    if not weather:
        return {"error": "Unable to fetch weather data"}

    real_time_rainfall = weather["rainfall"]

    # Dynamic month-wise values (use real-time rainfall + temperature influence)
    monthly_rainfall = np.array([real_time_rainfall * (1 + (weather["humidity"] / 100))] * 12)

    # Calculate seasonal averages
    Jan_Feb = np.mean(monthly_rainfall[:2])
    Mar_May = np.mean(monthly_rainfall[2:5])
    Jun_Sep = np.mean(monthly_rainfall[5:9])
    Oct_Dec = np.mean(monthly_rainfall[9:])

    # Model input features
    input_features = np.append(monthly_rainfall, [Jan_Feb, Mar_May, Jun_Sep, Oct_Dec]).reshape(1, -1)

    # Predict using the trained model
    predicted_rainfall = model.predict(input_features)[0]

    return {
        "city": city,
        "real_time_rainfall": round(real_time_rainfall, 2),
        "predicted_annual_rainfall": round(predicted_rainfall, 2),
        "temperature": weather["temperature"],
        "humidity": weather["humidity"],
        "weather_description": weather["weather_description"]
    }
