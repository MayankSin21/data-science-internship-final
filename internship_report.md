Internship Report
Name: Mayank Singh  
GitHub Repository: https://github.com/MayankSin21/data-science-internship-final

Introduction
During my internship at NULL CLASS, I had the opportunity to work on real-world Data Science projects aimed at applying Natural Language Processing (NLP) techniques to practical problems. This internship provided valuable hands-on experience and helped strengthen my understanding of various AI technologies.
Background
With the rise of AI and NLP technologies, there has been an increasing demand for intelligent systems capable of processing and understanding human language. This internship focused on developing two such systems: an extractive summarization tool and a medical Q\&A chatbot.
The tasks completed during the internship were not treated as isolated projects but were carefully designed to align with and extend the learning objectives of a data science curriculum. The extractive summarization task introduced fundamental text processing and NLP concepts, which were further utilized and enhanced in the medical Q&A chatbot. Together, these tasks form an integrated application of natural language processing (NLP), where summarization techniques can be embedded into chatbot responses for concise and informative user interaction. This reflects a real-world pipeline approach and demonstrates the application of course knowledge in building intelligent, user-centric systems.



Learning Objectives
* Understand and implement NLP techniques such as extractive summarization and information retrieval.
* Gain hands-on experience with real-world datasets (e.g., MedQuAD).
* Build applications that can summarize documents and answer user queries.
* Learn the workflow of data preprocessing, model development, evaluation, and deployment.
* Develop coding best practices and version control using GitHub.

Activities and Tasks
Task 1: Extractive Summarization
I developed a Python-based tool that implements extractive summarization using the TextRank algorithm. This tool analyzes the content of a long document and selects the most important sentences to form a concise summary.
* Loaded and cleaned text documents.
* Used TF-IDF vectorization to score sentence importance.
Selected top-ranked sentences to generate a summary.

Task 2: Medical Q\&A Chatbot
I built a simple chatbot that answers medical questions using the MedQuAD dataset.
* Parsed and cleaned XML files containing medical Q\&A pairs.
* Used TF-IDF-based cosine similarity to match user queries with relevant answers.
Created a functional chatbot interface for user interaction.

Task 3: Knowledge Base Updater
Created a scheduled script to dynamically update the chatbot’s knowledge base by embedding and indexing new entries.

Task 4: Multilingual Support
Integrated Google Translate and language detection to support English, Hindi, Bengali, and Marathi in the chatbot.

Task 5: Sentiment Analysis
Added sentiment analysis to detect positive, negative, or neutral user emotions and generate context-aware responses.

Skills and Competencies
- Python (NLTK, Scikit-learn, Pandas, Matplotlib)
- Streamlit (for chatbot UI)
- TF-IDF and cosine similarity
- Translation APIs (Googletrans)
- Langdetect, Transformers
- Git and GitHub
- Data preprocessing and embedding
Feedback and Evidence
* All tasks were documented with working code in Jupyter Notebooks.
* The projects were uploaded to GitHub with complete requirements files.
* Daily reports were submitted through the required Google Forms.

Challenges and Solutions
Challenge : Parsing complex XML files in MedQuAD dataset.
Solution : Wrote robust functions with error handling to skip malformed files.
Challenge : Identifying the most relevant answer from a large dataset.
Solution : Applied TF-IDF vectorization and cosine similarity for accurate retrieval.

Outcomes and Impact
This internship significantly improved my skills in:
- Full-cycle chatbot development
- NLP techniques for summarization and sentiment analysis
- Multilingual application design
- Working independently on real-world machine learning problems



Conclusion
This internship has been a valuable experience in applying Data Science skills to real-world projects. I have improved my technical skills, learned how to approach and solve real problems, and gained confidence in deploying AI-powered solutions. I look forward to applying these skills in future academic and professional endeavors.
