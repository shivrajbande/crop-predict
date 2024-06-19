import sys
import numpy as np
import pickle

# Load the model and scalers
model = pickle.load(open('model.pkl', 'rb'))
sc = pickle.load(open('standscaler.pkl', 'rb'))
ms = pickle.load(open('minmaxscaler.pkl', 'rb'))
print("shivraj")

# Get the feature list from the command line arguments
feature_list = list(map(float, sys.argv[1:]))
single_pred = np.array(feature_list).reshape(1, -1)
print(feature_list)

# Apply scaling
scaled_features = ms.transform(single_pred)
final_features = sc.transform(scaled_features)

# Make prediction
prediction = model.predict(final_features)

# Crop dictionary
crop_dict = {1: "Rice", 2: "Maize", 3: "Jute", 4: "Cotton", 5: "Coconut", 6: "Papaya", 7: "Orange",
             8: "Apple", 9: "Muskmelon", 10: "Watermelon", 11: "Grapes", 12: "Mango", 13: "Banana",
             14: "Pomegranate", 15: "Lentil", 16: "Blackgram", 17: "Mungbean", 18: "Mothbeans",
             19: "Pigeonpeas", 20: "Kidneybeans", 21: "Chickpea", 22: "Coffee"}

if prediction[0] in crop_dict:
    crop = crop_dict[prediction[0]]
    result = "{} is the best crop to be cultivated right there".format(crop)
else:
    result = "Sorry, we could not determine the best crop to be cultivated with the provided data."

print(result)
