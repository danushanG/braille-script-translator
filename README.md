# Automated Braille Script Processing System for Academic Institutions

This project is my final year undergraduate project, developed to help examiners and educators by automatically translating Braille into English text using AI.  
It combines **Flask (Python backend)**, **YOLOv8 (Braille dot detection)**, and **React (frontend)**.

---

## ✨ Features
- Upload a Braille image for translation  
- Camera scan to capture Braille in real time  
- Translation history stored locally  
- Export results as **PDF** or **audio (text-to-speech)**  
- Simple web-based user interface  

---

## 🖥 Requirements
Before running the system, please make sure you have installed:
- **Python 3.10+** → [Download](https://www.python.org/downloads/)  
- **Node.js 18+** → [Download](https://nodejs.org/en/download/)  
- **pip** (comes with Python)  
- **npm** (comes with Node.js)  

---

## ⚡ Setup Instructions

### 1. Clone or Download
- Clone using Git:
- git clone https://github.com/<your-username>/<repo-name>.git
- cd <repo-name>

## 2. Backend Setup (Flask + YOLOv8)

- Go to the backend folder: cd backend
- Install required Python packages: pip install -r requirements.txt
- Run the backend server: python app.py

## 3. Frontend Setup (React)

- Open a new terminal and go to the frontend folder: cd frontend
- Install required Node packages: npm install
- Run the frontend: npm start
➡️ This starts the frontend at: http://localhost:3000

## 🚀 Usage

- Open http://localhost:3000 in your browser.
- Upload a Braille image or use the Camera Scan feature.
- View the translated English text.
- Export results to PDF or play with audio output.

## ⚠️ Limitations

- Works best with small Braille samples (words/sentences).
- Does not support full A4 pages or paragraphs yet.
- Occasional misclassification may occur due to dataset limitations

## 📂 Project Structure
repo-name/
│
├── backend/        # Flask backend + YOLOv8 model
│   ├── app.py
│   ├── best.pt
│   └── requirements.txt
│
└── frontend/       # React frontend
    ├── src/
    ├── public/
    └── package.json

## 👤 Author

Ganeshan Danushan
Undergraduate – University of Kelaniya
Index No: CT/2019/032
