import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler, MinMaxScaler
import pickle

# Example dataset (replace with your actual dataset)
data = {
    'Nitrogen': [90, 85, 60, 78, 92, 80, 72, 75, 88, 94],
    'Phosporus': [42, 38, 56, 44, 41, 39, 49, 48, 46, 50],
    'Potassium': [60, 58, 62, 65, 70, 68, 63, 67, 64, 69],
    'Temperature': [20.5, 21.0, 19.8, 20.1, 21.3, 20.9, 19.7, 21.4, 20.2, 21.5],
    'Humidity': [80, 82, 78, 75, 79, 81, 77, 76, 78, 80],
    'Ph': [6.5, 6.8, 6.6, 6.7, 6.9, 6.4, 6.7, 6.6, 6.8, 6.5],
    'Rainfall': [200, 180, 210, 190, 205, 195, 185, 200, 198, 202],
    'Crop': [1, 2, 1, 2, 1, 3, 4, 5, 6, 7]  # Crop labels
}

df = pd.DataFrame(data)

# Features and target
X = df[['Nitrogen', 'Phosporus', 'Potassium', 'Temperature', 'Humidity', 'Ph', 'Rainfall']]
y = df['Crop']

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Preprocessing
sc = StandardScaler()
X_train_scaled = sc.fit_transform(X_train)
X_test_scaled = sc.transform(X_test)

ms = MinMaxScaler()
X_train_scaled_minmax = ms.fit_transform(X_train_scaled)
X_test_scaled_minmax = ms.transform(X_test_scaled)

# Train model
model = RandomForestClassifier()
model.fit(X_train_scaled_minmax, y_train)

# Save the model and scalers
pickle.dump(model, open('model.pkl', 'wb'))
pickle.dump(sc, open('standscaler.pkl', 'wb'))
pickle.dump(ms, open('minmaxscaler.pkl', 'wb'))

print("Model and scalers saved!")
