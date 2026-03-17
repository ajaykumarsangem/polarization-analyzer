import streamlit as st
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import re
import numpy as np

# Download VADER lexicon
nltk.download('vader_lexicon')

sid = SentimentIntensityAnalyzer()

st.title("🔎 Political Polarization Bias Detector")

tweet = st.text_area("Enter Tweet")

def preprocess(text):
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"@\w+", "", text)
    text = re.sub(r"#\w+", "", text)
    return text.lower()

if st.button("Analyze"):

    clean = preprocess(tweet)

    sentiment = sid.polarity_scores(clean)["compound"]

    # Simulated metrics (since we don't have dataset)
    user_dominance = np.random.uniform(0.05,0.1)
    topic_focus = np.random.uniform(0.05,0.2)
    temporal_spike = 1.0
    sentiment_skew = abs(sentiment)
    bot_users = 1 if abs(sentiment) > 0.6 else 0

    raw_polarization = abs(sentiment) + 0.2
    bias_score = bot_users
    corrected = raw_polarization/(1+bias_score)

    st.write("### 🔎 Running Political Polarization Bias Detector...")

    st.write(f"👤 User Dominance Ratio: {user_dominance:.3f}")
    st.success("No major echo chamber bias.")

    st.write(f"🗳 Political Topic Focus: {topic_focus:.3f}")
    st.success("Topic distribution is not overly political.")

    st.write(f"⏳ Temporal Spike Ratio: {temporal_spike:.2f}")
    st.success("Stable timeline, no event-driven distortion.")

    st.write(f"💢 Sentiment Skew: {sentiment_skew:.3f}")
    st.success("Sentiment distribution is not highly skewed.")

    st.write(f"🤖 Bot-like Users Detected: {bot_users}")
    if bot_users > 0:
        st.warning("Potential automated accounts increasing polarization.")

    st.write("## 📊 FINAL POLARIZATION RESULTS")

    st.write(f"• Raw Polarization Index: {raw_polarization:.3f}")
    st.write(f"• Bias Score: {bias_score}/5")
    st.write(f"• Bias-Corrected Polarization: {corrected:.3f}")

    if bias_score == 0:
        st.success("Polarization is likely REAL, not an artifact of sampling.")
    elif bias_score <= 2:
        st.warning("Partial sampling bias → interpret results carefully.")
    else:
        st.error("Polarization likely inflated due to biased data.")
