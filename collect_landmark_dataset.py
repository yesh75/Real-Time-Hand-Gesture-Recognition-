import cv2
import mediapipe as mp
import numpy as np
import os
import json

SAVE_DIR = "dataset_landmarks"
os.makedirs(SAVE_DIR, exist_ok=True)

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_draw = mp.solutions.drawing_utils

LETTERS = list("ABCDEFGHIJKLMNOPQRSTUVWXY")

cap = cv2.VideoCapture(0)

print("=== ASL Landmark Dataset Collector ===")
print("Press SPACE to save sample, N to next letter, Q to quit")

for letter in LETTERS:
    letter_dir = os.path.join(SAVE_DIR, letter)
    os.makedirs(letter_dir, exist_ok=True)
    print(f"\nCollecting for letter: {letter}")

    while True:
        ret, frame = cap.read()
        if not ret: break
        frame = cv2.flip(frame, 1)
        h, w = frame.shape[:2]

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb)

        if results.multi_hand_landmarks:
            lm = results.multi_hand_landmarks[0]
            mp_draw.draw_landmarks(frame, lm, mp_hands.HAND_CONNECTIONS)

            # Extract landmark coords
            landmarks = []
            for p in lm.landmark:
                landmarks.extend([p.x, p.y, p.z])

        else:
            landmarks = None

        cv2.putText(frame, f"Letter: {letter}", (10, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)

        cv2.imshow("Collect Landmarks", frame)
        key = cv2.waitKey(1) & 0xFF

        if key == ord(' '):
            if landmarks:
                filename = os.path.join(letter_dir, f"{len(os.listdir(letter_dir))}.json")
                with open(filename, "w") as f:
                    json.dump(landmarks, f)
                print("Saved landmark:", filename)

        elif key in (ord('n'), ord('N')):
            break

        elif key in (ord('q'), ord('Q')):
            cap.release()
            cv2.destroyAllWindows()
            exit()

cap.release()
cv2.destroyAllWindows()
