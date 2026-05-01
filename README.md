✋ Hand Gesture Recognition System
<p align="center"> Real-time hand gesture recognition using computer vision and MediaPipe </p> <p align="center"> <img src="https://img.shields.io/badge/Python-3.x-blue" /> <img src="https://img.shields.io/badge/OpenCV-Computer%20Vision-green" /> <img src="https://img.shields.io/badge/MediaPipe-Hand%20Tracking-orange" /> <img src="https://img.shields.io/badge/Status-Active-success" /> </p>
Overview

This project implements a real-time hand gesture recognition system using a webcam feed. It detects hand landmarks and classifies gestures based on finger positions.

The goal is to explore touchless human-computer interaction using lightweight and efficient computer vision techniques.

Key Features
Real-time hand detection and tracking
Landmark-based gesture recognition (21 key points)
Fast and efficient processing
Modular and easy-to-extend code structure
Tech Stack
Category	Tools Used
Language	Python
Computer Vision	OpenCV
Hand Tracking	MediaPipe
Utilities	NumPy
System Workflow
Webcam Input → Hand Detection → Landmark Extraction → Gesture Logic → Output
Project Structure
hand-gesture-recognition/
│
├── main.py            # Main execution file
├── detector.py        # Hand detection module
├── gestures.py        # Gesture recognition logic
├── requirements.txt   # Project dependencies
└── README.md
Installation & Setup
1. Clone Repository
git clone https://github.com/your-username/hand-gesture-recognition.git
cd hand-gesture-recognition
2. Install Dependencies
pip install -r requirements.txt
3. Run the Application
python main.py
Example Gestures
👍 Thumbs Up
✋ Open Palm
✊ Fist
☝️ Pointing
   



Limitations
Sensitive to lighting conditions
Limited gesture set (rule-based detection)
Accuracy may vary with camera quality
🔮 Future Improvements
Integration with ML/DL models
Dynamic gesture recognition
Multi-hand tracking
Real-world application integration (mouse control, IoT, etc.)
Contribution

Contributions are welcome. Feel free to fork and submit a pull request.

License

This project is licensed under the MIT License.

Author

Yesh Chandra Joshi
MCA Student | Computer Vision Enthusiast

Support

If you find this project useful, consider giving it a ⭐ on GitHub.
