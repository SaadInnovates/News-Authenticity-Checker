# News-Authenticity-Checker

This is a simple **Fake News Detection Web App** built using **Streamlit** and **Machine Learning**. It classifies news articles as **Fake** or **Real** based on the title and content using NLP techniques and a trained model.

---

## 🚀 Demo

![App Screenshot](https://github.com/your-username/fake-news-detector/assets/demo.gif)  
*(Insert a GIF or image of your app here)*

---

## 📦 Features

- Input: News **Title** and **Text**
- NLP Preprocessing: Tokenization, Stopword Removal, Stemming
- TF-IDF Vectorization
- Classification using a trained ML model (e.g., Logistic Regression, Naive Bayes, etc.)
- Web UI using Streamlit

---

## 🧠 Tech Stack

- Python 🐍
- Streamlit 🌐
- NLTK (Natural Language Toolkit)
- scikit-learn
- pickle (for model persistence)

---

## 📁 Project Structure
fake-news-detector/
│
├── app.py # Streamlit frontend
├── vectorizer.pkl # Saved TF-IDF Vectorizer
├── model.pkl # Trained ML Model
├── requirements.txt # Python dependencies
└── README.md # Project documentation



---

## 🛠️ Installation

1. **Clone the repository**  
```bash
git clone https://github.com/your-username/fake-news-detector.git
cd fake-news-detector


```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Run the app**
```bash
streamlit run app.py
```



