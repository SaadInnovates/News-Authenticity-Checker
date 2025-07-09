import streamlit as st
import pickle
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

# Download necessary NLTK resources
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')

# Initialize stemmer
ps = PorterStemmer()

# Text preprocessing function
def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)

# Load vectorizer and model
tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))

# Streamlit UI
st.title("📰 Fake News Detector")

# Input fields
news_title = st.text_input("Enter News Title")
news_text = st.text_area("Enter News Content")

# Predict button
if st.button('Predict'):
    # Input validation
    if not news_title.strip() or not news_text.strip():
        st.warning("⚠️ Please enter both the News Title and News Content.")
    else:
        # Combine title and content
        full_text = news_title + " " + news_text

        # Transform the text
        transformed_input = transform_text(full_text)

        # Vectorize
        vector_input = tfidf.transform([transformed_input])

        # Predict
        result = model.predict(vector_input)[0]

        # Display result
        if result == 1:
            st.success("✅ This is **Real News**.")
        else:
            st.error("🛑 This is **Fake News**.")
