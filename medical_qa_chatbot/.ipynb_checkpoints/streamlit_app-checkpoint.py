import streamlit as st
import pandas as pd
import joblib
from sklearn.metrics.pairwise import cosine_similarity

# Load saved components
df = pd.read_csv("saved_model/medquad_qa.csv")
vectorizer = joblib.load("saved_model/vectorizer.pkl")
X = joblib.load("saved_model/X.pkl")

def get_answer(user_input):
    user_vec = vectorizer.transform([user_input])
    similarity = cosine_similarity(user_vec, X).flatten()
    best_idx = similarity.argmax()
    return df.iloc[best_idx]["answer"]

# UI
st.title("🩺 Medical Q&A Chatbot")
st.write("Ask a health-related question")

user_input = st.text_input("Your Question:")

if user_input:
    answer = get_answer(user_input)
    st.write("**Answer:**", answer)