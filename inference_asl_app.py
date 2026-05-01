import cv2
import mediapipe as mp
import numpy as np
import pickle
import threading
import pyttsx3

# ============ SPEECH ============
def speak_async(text):
    def run_tts():
        engine = pyttsx3.init('sapi5')
        engine.setProperty('rate', 170)
        engine.say(text)
        engine.runAndWait()
    threading.Thread(target=run_tts, daemon=True).start()

# ============ LOAD MODEL ============
with open("model/asl_landmark_model.pkl", "rb") as f:
    model = pickle.load(f)

# ============ MEDIAPIPE ============
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_draw = mp.solutions.drawing_utils

# ============ SENTENCE BUFFER ============
sentence = ""
current_letter = "-"
smooth_buffer = []

cap = cv2.VideoCapture(0)

print("Controls:")
print(" ENTER = add letter")
print(" SPACE = add space")
print(" S = speak sentence")
print(" C = clear sentence")
print(" BACKSPACE = delete")
print(" Q = quit")

while True:
    ret, frame = cap.read()
    if not ret: break
    frame = cv2.flip(frame, 1)
    h, w = frame.shape[:2]

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    res = hands.process(rgb)

    current_letter = "-"

    if res.multi_hand_landmarks:
        lm = res.multi_hand_landmarks[0]
        mp_draw.draw_landmarks(frame, lm, mp_hands.HAND_CONNECTIONS)

        feat = []
        for p in lm.landmark:
            feat.extend([p.x, p.y, p.z])

        pred = model.predict([feat])[0]

        smooth_buffer.append(pred)
        if len(smooth_buffer) > 7:
            smooth_buffer.pop(0)

        current_letter = max(set(smooth_buffer), key=smooth_buffer.count)

    # ========= UI ============
    cv2.putText(frame, f"Current: {current_letter}", (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)

    cv2.putText(frame, f"Sentence: {sentence}", (20, 80),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)

    cv2.imshow("ASL Recognition", frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'): break
    if key == 13 and current_letter != "-": sentence += current_letter
    if key == 32: sentence += " "
    if key == ord('s'):
        if sentence.strip(): speak_async(sentence)
    if key == ord('c'): sentence = ""
    if key == 8: sentence = sentence[:-1]

cap.release()
cv2.destroyAllWindows()
