import os, json
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import pickle

DATA_DIR = "dataset_landmarks"

X = []
y = []

for label in os.listdir(DATA_DIR):
    folder = os.path.join(DATA_DIR, label)
    for file in os.listdir(folder):
        path = os.path.join(folder, file)
        with open(path, "r") as f:
            landmarks = json.load(f)
        X.append(landmarks)
        y.append(label)

X = np.array(X)
y = np.array(y)

print("Training on:", X.shape, "samples")

model = RandomForestClassifier(n_estimators=300)
model.fit(X, y)

os.makedirs("model", exist_ok=True)
with open("model/asl_landmark_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model saved!")
