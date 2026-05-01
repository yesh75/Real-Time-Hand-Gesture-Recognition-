from flask import Flask, request, jsonify
from flask_cors import CORS
import cv2
import numpy as np
import mediapipe as mp
import pickle
import base64

# Load ASL Model
with open("model/asl_landmark_model.pkl", "rb") as f:
    model = pickle.load(f)

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)

app = Flask(__name__)
CORS(app)

def extract_landmarks(image):
    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)

    if results.multi_hand_landmarks:
        lm = results.multi_hand_landmarks[0]
        landmarks = []
        for p in lm.landmark:
            landmarks.extend([p.x, p.y, p.z])
        return landmarks
    return None

@app.post("/predict")
def predict():
    data = request.json["image"]

    # Convert BASE64 → numpy array
    img_bytes = base64.b64decode(data.split(",")[1])
    np_arr = np.frombuffer(img_bytes, np.uint8)
    image = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

    # Extract hand landmarks
    landmarks = extract_landmarks(image)
    if landmarks is None:
        return jsonify({"letter": "-"})

    # Predict letter
    letter = model.predict([landmarks])[0]
    return jsonify({"letter": letter})

if __name__ == "__main__":
    print("Flask server running on http://127.0.0.1:5000")
    app.run(host="0.0.0.0", port=5000)
