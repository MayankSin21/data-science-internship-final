✅ Task 2: Medical Q&A Chatbot

This chatbot uses the MedQuAD dataset to answer health-related queries. It finds the most relevant match using TF-IDF and cosine similarity.

## How it works

- Input a question like: `what is psychogenic movement?`
- It finds the most similar question from MedQuAD.
- Returns the matched question + answer.

## Files

- `chatbot.ipynb` – Full code
- `medquad_qa.csv` – CSV created from MedQuAD XML files
- `saved_model/` – Saved TF-IDF vectorizer and question matrix

## Run Instructions

1. Open `chatbot.ipynb` in Jupyter Notebook
2. Run all cells
3. Start asking medical questions!

## Dataset Credit

MedQuAD dataset © U.S. National Library of Medicine

---

✅ Task 3: Dynamic Knowledge Base Updater

This task implements a system that updates the chatbot’s knowledge base with new Q&A data.

### How it Works:
- Adds new entries from `new_data.csv`
- Merges with existing `medquad_qa.csv`
- Rebuilds the TF-IDF vectorizer and saves the new model

### To Run:
```bash
python knowledge_updater.py

✅ Task 4: Multilingual Chatbot Support

This module allows the chatbot to detect the user’s language and respond accordingly.  
Supported Languages: English, Hindi, Bengali, Tamil

Features:
- Automatic language detection using `langdetect`
- Real-time translation via `googletrans`
- Uses the same TF-IDF response system from Task 2

To Run:
- Use the notebook: `multilingual_chatbot.ipynb`

✅ Task 5: Sentiment Analysis Integration

This module enhances the multilingual chatbot with sentiment detection.  
It uses TextBlob to detect whether the user input is positive, negative, or neutral.

- Library used: TextBlob
- Languages supported: Multilingual
- How it works:
  - Detects language using `langdetect`
  - Translates to English using `googletrans`
  - Runs sentiment detection using `TextBlob`
  - Retrieves best matching answer using TF-IDF
  - Wraps response with emotional tone (e.g., "I'm sorry to hear that")

### 🔄 Example
You: I’m feeling anxious about my chest pain.
Bot: I'm sorry to hear that. Chest pain can be caused by many conditions. ...