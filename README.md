# 📊 Data Science Internship – Nullclass

This repository contains the completed work for the **Nullclass Data Science Internship** (May–July 2025), fulfilling all 5 assigned tasks including NLP, chatbot development, multilingual support, and sentiment analysis.

---

## 📂 Folder Structure

data-science-internship-final/
├── extractive_summarizer/
│ ├── summarizer.ipynb
│ ├── sample_text.txt
│ ├── requirements.txt
│ └── README.md
│
├── medical_qa_chatbot/
│ ├── chatbot.ipynb
│ ├── multilingual_chatbot.ipynb
│ ├── sentiment_chatbot.ipynb
│ ├── knowledge_updater.py
│ ├── medquad_qa.csv
│ ├── new_data.csv
│ ├── requirements.txt
│ └── saved_model/
│
├── internship_report.md
└── README.md

---

## ✅ Tasks Completed

### Task 1: Extractive Summarizer
- Extracts key sentences from long documents using TF-IDF.
- Input: Plain text files.
- Output: Concise summaries.

### Task 2: Medical Q&A Chatbot
- Uses MedQuAD dataset to answer health-related queries.
- Employs TF-IDF vector search and cosine similarity.

### Task 3: Knowledge Base Updater
- Adds new QA pairs to the chatbot.
- Converts questions and answers to vector space using TF-IDF.

### Task 4: Multilingual Support
- Supports 4 languages: English, Hindi, Bengali, Marathi.
- Detects and translates input queries and responses using Google Translate.

### Task 5: Sentiment Analysis
- Detects user sentiment (positive/negative/neutral).
- Alters chatbot response based on user emotion.

---

## 🚀 Technologies Used

- Python, Scikit-learn, Pandas, NLTK, Streamlit
- Googletrans, langdetect
- TF-IDF, cosine similarity
- Git & GitHub

---

## 📦 Installation

1. Clone the repository:
```bash
git clone https://github.com/MayankSin21/data-science-internship-final.git
cd data-science-internship-final

cd extractive_summarizer
pip install -r requirements.txt

cd ../medical_qa_chatbot
pip install -r requirements.txt

