# 🚫 Restricted Content Detection in Videos Using AI

This project is an AI-powered web application that detects **restricted content** in videos, including **visual violence** and **offensive/profane language**. It uses **YOLOv8** for violence detection and **speech-to-text** with keyword filtering for identifying profanity.

---

## 📌 Features

- ✅ Upload videos through a simple UI
- 🧠 Detects violence using a custom-trained YOLOv8 model
- 🔊 Transcribes audio and detects profane language
- 💻 Frontend built with React
- 🔧 Backend using Node.js + Express, runs Python for detection
- 🧪 Custom dataset from Kaggle used for model training

---

## 🧰 Technologies Used

| Layer       | Technology                                     |
|-------------|------------------------------------------------|
| Frontend    | React, JavaScript, HTML, Tailwind CSS          |
| Backend     | Node.js, Express, Multer, Child Process (spawn)|
| AI Models   | YOLOv8 (Ultralytics), SpeechRecognition        |
| Audio Tools | `pydub`, `ffmpeg-python`, `ffmpeg`             |
| Python Side | Python 3.12+, OpenCV, Ultralytics, Google STT  |

---

## 📁 Project Structure
restricted_content_detector_starter/ ├── backend/ │ └── server.js # Node.js backend server ├── scripts/ │ └── run_detection.py # Python script with YOLO + Audio logic ├── frontend/ # React app │ ├── src/ │ └── ... ├── uploads/ # Temporarily stores uploaded videos ├── model/ # Trained YOLOv8 weights (best.pt) ├── README.md └── .gitignore


🚀 How to Run
1. Clone the Repository
2. git clone https://github.com/yourusername/restricted-content-detector.git
cd restricted-content-detector
2. Setup Backend (Node.js)
bash
Copy
Edit
cd backend
npm install
node server.js
Backend runs at: http://localhost:5000

3. Setup Frontend (React)
bash
Copy
Edit
cd frontend
npm install
npm run dev
Frontend runs at: http://localhost:5173 (default Vite port)

4. Python Environment Setup
Make sure Python 3.12+ is installed.

Install Python dependencies:

bash
Copy
Edit
pip install ultralytics opencv-python SpeechRecognition pydub ffmpeg-python
Also make sure ffmpeg is installed and added to system PATH:

bash
Copy
Edit
ffmpeg -version
🧠 AI Models
YOLOv8 is trained to detect violence from video frames.

Speech-to-text: Uses Google Web Speech API to transcribe audio and match profanity keywords.

🔎 Sample Profanity Keywords
python
Copy
Edit
["damn", "hell", "shit", "fuck", "bitch", "violence", "kill", "murder", "rape", "terrorist"]
You can edit the list in run_detection.py.


✅ requirements.txt (Python side)
txt
Copy
Edit
ultralytics
opencv-python
SpeechRecognition
pydub
ffmpeg-python
You can use pip install -r requirements.txt to install them all.
