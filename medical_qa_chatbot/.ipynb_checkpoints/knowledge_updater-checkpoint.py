import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import joblib
import os

def update_knowledge(base_csv='medquad_qa.csv', new_csv='new_data.csv'):
    base_df = pd.read_csv(base_csv)
    new_df = pd.read_csv(new_csv)

    combined_df = pd.concat([base_df, new_df]).drop_duplicates().dropna()
    combined_df.to_csv(base_csv, index=False)

    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(combined_df['question'])

    os.makedirs('saved_model', exist_ok=True)
    joblib.dump(vectorizer, 'saved_model/vectorizer.pkl')
    joblib.dump(X, 'saved_model/X.pkl')

    print("✅ Knowledge base updated! Total entries:", len(combined_df))

if __name__ == "__main__":
    update_knowledge()