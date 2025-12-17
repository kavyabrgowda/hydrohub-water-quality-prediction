import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
from io import BytesIO
import base64

# Load Dataset
df = pd.read_csv("water_quality.csv")

# Drop unnecessary columns
df = df[['pH', 'EC', 'CO3', 'HCO3', 'Cl', 'SO4', 'NO3', 'Ca', 'Mg', 'Na', 'K', 'F', 'tds', 'WQI']]  # Keeping relevant features

# Handle missing values
df.dropna(inplace=True)

# Split data into features (X) and target (y)
X = df.drop(columns=['WQI'])  # Features
y = df['WQI']  # Target (Water Quality Index)

# Train-test split (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the model
model = RandomForestRegressor(n_estimators=100, random_state=42)

# Train the model
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Model Evaluation
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

print(f"Model RMSE: {rmse}")
print(f"Model R² Score: {r2}")

def calculate_wqi(ph, tds, hardness):
    # Weighted formula for WQI calculation
    wqi = (ph * 0.3) + (tds * 0.4) + (hardness * 0.3)
    
    if wqi <= 50:
        classification = "Excellent (Safe for drinking)"
    elif 51 <= wqi <= 100:
        classification = "Good (Minor treatment needed)"
    elif 101 <= wqi <= 200:
        classification = "Moderate (Filtration required)"
    elif 201 <= wqi <= 300:
        classification = "Poor (Needs purification before use)"
    elif 301 <= wqi <= 400:
        classification = "Very Poor (Not suitable for drinking, high risk)"
    elif 401 <= wqi <= 500:
        classification = "Severely Contaminated (Avoid drinking, high health risk)"
    elif 501 <= wqi <= 1000:
        classification = "Highly Polluted (Not for any domestic use)"
    elif 1001 <= wqi <= 2000:
        classification = "Extremely Polluted (Only suitable for industrial use)"
    elif 2001 <= wqi <= 3000:
        classification = "Toxic Water (Unsafe for any use, needs extreme treatment)"
    elif 3001 <= wqi <= 4000:
        classification = "Hazardous (Severe chemical contamination, environmental risk)"
    elif 4001 <= wqi <= 5000:
        classification = "Extremely Hazardous (Complete restriction on use)"
    else:
        classification = "Beyond Measurement (Immediate action required, potential disaster)"
    
    return wqi, classification

# Apply classification to predictions
df_test = X_test.copy()
df_test['Actual_WQI'] = y_test
df_test['Predicted_WQI'] = y_pred

# Calculate classification for each predicted WQI
df_test[['Calculated_WQI', 'Classification']] = df_test.apply(lambda row: calculate_wqi(row['pH'], row['tds'], row['Ca'] + row['Mg']), axis=1, result_type='expand')

# Save results to CSV
df_test.to_csv("predicted_wqi_results.csv", index=False)

print("Predictions saved to predicted_wqi_results.csv")


