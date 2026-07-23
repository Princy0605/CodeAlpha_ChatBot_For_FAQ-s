# 🤖 FAQ Chatbot using NLP & Cosine Similarity

An intelligent FAQ Chatbot built using **Python**, **Streamlit**, **NLTK**, and **Scikit-Learn**. This chatbot leverages **Natural Language Processing (NLP)** techniques to understand user queries and retrieve the most relevant answer from a predefined FAQ dataset using **TF-IDF Vectorization** and **Cosine Similarity**.

---

## 📌 Overview

The chatbot is designed to answer frequently asked questions by comparing the user's query with a collection of FAQs. Instead of relying on exact keyword matching, it uses NLP preprocessing and vector similarity to identify the most relevant question and return its corresponding answer.

This project demonstrates the practical application of NLP concepts such as text preprocessing, feature extraction, and similarity matching in an interactive web application.

---

## ✨ Features

- 📂 Loads FAQ data dynamically from a CSV file.
- 🧹 Performs text preprocessing using **NLTK**:
  - Lowercasing
  - Tokenization
  - Stop-word removal
  - Lemmatization
- 📊 Converts text into numerical vectors using **TF-IDF Vectorization**.
- 🔍 Finds the most relevant FAQ using **Cosine Similarity**.
- 💬 Interactive chatbot interface built with **Streamlit**.
- ⚡ Fast and lightweight implementation.
- 🚫 Returns a fallback response when no suitable match is found.
- 🔄 Easy to update by simply editing the `faq.csv` file.

---

## 🛠️ Technologies Used

- Python
- Streamlit
- NLTK
- Scikit-Learn
- NumPy
- CSV

---

## 📂 Project Structure

```text
FAQ_Chatbot/
│
├── app.py                 # Main Streamlit application
├── faq.csv                # FAQ dataset
├── download_nltk.py       # Downloads required NLTK resources
├── requirements.txt       # Project dependencies
├── .gitignore             # Git ignore rules
├── README.md              # Project documentation
└── venv/                  # Virtual environment (ignored by Git)
```

---

## 📋 Dataset

The chatbot uses a simple **CSV file (`faq.csv`)** as its knowledge base.

Each row contains:

- **Question**
- **Answer**

You can easily add, remove, or modify FAQs without changing the application code.

Example:

| Question | Answer |
|----------|--------|
| How can I reset my password? | Click on **Forgot Password** on the login page. |
| What are your operating hours? | Monday to Friday, 9 AM – 6 PM. |


---

## 🚀 How It Works

1. Loads FAQs from the CSV dataset.
2. Preprocesses all FAQ questions using NLTK.
3. Converts processed questions into TF-IDF vectors.
4. Accepts a user query through the Streamlit interface.
5. Preprocesses the user's query.
6. Converts the query into a TF-IDF vector.
7. Computes Cosine Similarity between the query and all FAQ questions.
8. Returns the answer corresponding to the highest similarity score.
9. Displays a fallback message if no relevant match is found.

---

## 📈 NLP Pipeline

```text
User Question
      │
      ▼
Text Preprocessing
(Lowercase, Tokenization,
Stopword Removal, Lemmatization)
      │
      ▼
TF-IDF Vectorization
      │
      ▼
Cosine Similarity
      │
      ▼
Best Matching FAQ
      │
      ▼
Return Answer
```

---

## 🎯 Future Improvements

- Voice input support
- Text-to-Speech responses
- Multi-language support
- Semantic Search using Sentence Transformers
- Integration with Large Language Models (LLMs)
- Admin panel for managing FAQs
- Database integration (MySQL/MongoDB)

---

## 👨‍💻 Author

**Princy Jain**


---

## 📄 License

This project is developed for learning purposes as part of the **CodeAlpha AI Internship**.