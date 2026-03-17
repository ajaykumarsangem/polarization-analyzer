import streamlit as st
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import re

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

    st.subheader("Results")

    st.write("Cleaned Tweet:", clean)
    st.write("Sentiment Score:", score)

    if score > 0.05:
        st.success("Positive Sentiment")
    elif score < -0.05:
        st.error("Negative Sentiment")
    else:
        st.info("Neutral Sentiment")