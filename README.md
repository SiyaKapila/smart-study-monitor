# 🎓 Smart Study Monitor

**Smart Study Monitor** is a Python-based AI study assistant developed as a university project to explore concepts in Machine Learning, Computer Vision, and modular software design.
The system helps students track study sessions, analyze learning difficulty from notes, and simulate focus monitoring using OpenCV.

---

## 📌 Overview

This project demonstrates how Artificial Intelligence techniques can be applied to improve study habits. It combines:

* ⏱ **Study Session Tracking** – Record and analyze study durations
* 🧠 **Confusion Prediction (NLP)** – Classify notes as *easy* or *risk/confusing*
* 👁 **Focus Detection** – Basic face detection using OpenCV
* 📊 **Analytics Storage** – Local CSV-based data tracking

---

## 🧩 Project Structure

```
smart-study-monitor/
├── main.py        # Entry point and CLI menu
├── monitor.py     # Study timer logic
├── model.py       # Machine learning predictor
├── analytics.py   # Data storage and statistics
├── vision.py      # OpenCV focus detection
└── README.md
```

---

## ⚙️ Technologies Used

* **Python 3**
* **scikit-learn** – NLP classification model
* **OpenCV** – Computer vision (face detection)
* **Pandas** – Data handling and analytics

---

## 🚀 Installation & Setup

Clone the repository:

```
git clone https://github.com/YOUR-USERNAME/smart-study-monitor.git
cd smart-study-monitor
```

Install dependencies:

```
pip3 install scikit-learn pandas opencv-python
```

Run the project:

```
python3 main.py
```

---

## ▶️ Usage

After running the program, select options from the terminal:

```
1. Start Study
2. End Study
3. Analyze Notes
4. Show Analytics
5. Exit
6. Check Focus (OpenCV)
```

---

## 🎯 Academic Objectives

This project was built to demonstrate:

* Object-Oriented Programming in Python
* Basic Natural Language Processing workflow
* Introductory Computer Vision concepts
* Clean modular project architecture
