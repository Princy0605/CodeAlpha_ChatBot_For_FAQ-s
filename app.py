import streamlit as st
import csv
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# 1. Ensure required NLTK resources are available locally
@st.cache_resource
def setup_nltk():
    nltk.download('punkt', quiet=True)
    nltk.download('punkt_tab', quiet=True)
    nltk.download('stopwords', quiet=True)
    nltk.download('wordnet', quiet=True)

setup_nltk()

lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

# 2. Pure NLTK Preprocessing Function
def preprocess_text(text):
    text = text.lower()
    tokens = word_tokenize(text)
    cleaned_tokens = [
        lemmatizer.lemmatize(word)
        for word in tokens
        if word.isalpha() and word not in stop_words
    ]
    return " ".join(cleaned_tokens)

# 3. Load FAQs dynamically from the faq.csv file
@st.cache_data
def load_faqs_from_csv(file_path="faq.csv"):
    questions = []
    answers = []
    try:
        with open(file_path, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                questions.append(row["Question"])
                answers.append(row["Answer"])
    except FileNotFoundError:
        st.error(f"File '{file_path}' not found! Make sure faq.csv is placed in the same folder as app.py.")
        return [], []
    
    return questions, answers

# Read questions and answers from CSV
raw_questions, answers = load_faqs_from_csv("faq.csv")

# 4. TF-IDF Vectorizer Setup
@st.cache_resource
def build_vectorizer(questions):
    if not questions:
        return None, None
    cleaned_questions = [preprocess_text(q) for q in questions]
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(cleaned_questions)
    return vectorizer, tfidf_matrix

vectorizer, tfidf_matrix = build_vectorizer(raw_questions)

# 5. Matching Logic using Cosine Similarity
def get_best_answer(user_query, threshold=0.15):
    if not vectorizer or tfidf_matrix is None:
        return "FAQ data is not loaded properly. Please check your faq.csv file."

    processed_query = preprocess_text(user_query)
    
    if not processed_query.strip():
        return "Please ask a more specific question!"
    
    query_vector = vectorizer.transform([processed_query])
    similarities = cosine_similarity(query_vector, tfidf_matrix).flatten()
    
    best_idx = similarities.argmax()
    best_score = similarities[best_idx]
    
    if best_score < threshold:
        return "I'm sorry, I couldn't find an answer to that in our FAQs. Please try rephrasing or contact support."
    
    return answers[best_idx]

# 6. Streamlit Chat UI
st.set_page_config(page_title="FAQ Chatbot", page_icon="🤖")
st.title("🤖 FAQ Assistant")
st.caption("Connected to `faq.csv` | Built with Streamlit, NLTK, & Scikit-learn")

# Initialize Chat State
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display prior chat messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User Chat Input
if prompt := st.chat_input("Ask a question..."):
    # Add user message to UI
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Compute response and add to UI
    bot_response = get_best_answer(prompt)
    st.session_state.messages.append({"role": "assistant", "content": bot_response})
    with st.chat_message("assistant"):
        st.markdown(bot_response)