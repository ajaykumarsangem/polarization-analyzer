import streamlit as st
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import re

# Download VADER lexicon
nltk.download('vader_lexicon')

sid = SentimentIntensityAnalyzer()

st.title("Social Media Polarization Analyzer")

tweet = st.text_area("Enter Tweet")

def preprocess(text):
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"@\w+", "", text)
    text = re.sub(r"#\w+", "", text)
    return text.lower()

if st.button("Analyze"):
    clean = preprocess(tweet)

    score = sid.polarity_scores(clean)["compound"]

    st.write("Cleaned Tweet:", clean)
    st.write("Sentiment Score:", score)
