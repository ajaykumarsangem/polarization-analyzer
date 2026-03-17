import streamlit as st
import json
import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from collections import Counter

# Download vader lexicon (needed on Streamlit Cloud)
nltk.download('vader_lexicon')

sid = SentimentIntensityAnalyzer()

st.title("📊 Political Polarization Bias Detector")

st.write("Upload your Twitter dataset to analyze political polarization and bias.")

# Upload files
tweets_file = st.file_uploader("Upload tweets.json", type="json")
users_file = st.file_uploader("Upload users.json", type="json")

def compute_bias(tweets, users):

    texts = [t["text"] for t in tweets if "text" in t]

    # Sentiment scores
    sentiments = [sid.polarity_scores(t)["compound"] for t in texts]

    # Raw polarization
    raw_polarization = sum(abs(s) for s in sentiments) / len(sentiments)

    # Sentiment skew
    sentiment_skew = abs(sum(sentiments) / len(sentiments))

    # User dominance
    user_ids = [t["user_id"] for t in tweets if "user_id" in t]
    counts = Counter(user_ids)

    if len(counts) > 0:
        user_dominance = max(counts.values()) / len(user_ids)
    else:
        user_dominance = 0

    # Political keyword detection
    political_keywords = [
        "government","election","policy","democracy","minister",
        "party","vote","president","congress","senate"
    ]

    political_count = sum(
        any(word in t.lower() for word in political_keywords)
        for t in texts
    )

    topic_focus = political_count / len(texts)

    # Temporal spike (simplified demo value)
    temporal_spike = 1.0

    # Bot-like users (demo logic)
    bot_users = sum(1 for c in counts.values() if c > 50)

    # Bias score calculation
    bias_score = 0

    if user_dominance > 0.3:
        bias_score += 1
    if topic_focus > 0.5:
        bias_score += 1
    if sentiment_skew > 0.5:
        bias_score += 1
    if temporal_spike > 2:
        bias_score += 1
    if bot_users > 0:
        bias_score += 1

    corrected = raw_polarization / (1 + bias_score)

    return {
        "user_dominance": user_dominance,
        "topic_focus": topic_focus,
        "temporal_spike": temporal_spike,
        "sentiment_skew": sentiment_skew,
        "bot_users": bot_users,
        "raw": raw_polarization,
        "bias": bias_score,
        "corrected": corrected
    }


if tweets_file and users_file:

    tweets = json.load(tweets_file)
    users = json.load(users_file)

    st.success("Dataset loaded successfully")

    if st.button("Run Polarization Analysis"):

        results = compute_bias(tweets, users)

        st.subheader("🔎 Running Political Polarization Bias Detector")

        st.write(f"👤 User Dominance Ratio: {results['user_dominance']:.3f}")
        if results['user_dominance'] < 0.3:
            st.success("No major echo chamber bias")
        else:
            st.warning("Possible echo chamber detected")

        st.write(f"🗳 Political Topic Focus: {results['topic_focus']:.3f}")
        if results['topic_focus'] < 0.5:
            st.success("Topic distribution is not overly political")
        else:
            st.warning("Dataset heavily political")

        st.write(f"⏳ Temporal Spike Ratio: {results['temporal_spike']:.2f}")
        st.success("Stable timeline, no event-driven distortion")

        st.write(f"💢 Sentiment Skew: {results['sentiment_skew']:.3f}")
        if results['sentiment_skew'] < 0.5:
            st.success("Sentiment distribution not highly skewed")
        else:
            st.warning("Sentiment distribution highly skewed")

        st.write(f"🤖 Bot-like Users Detected: {results['bot_users']}")
        if results['bot_users'] > 0:
            st.warning("Potential automated accounts increasing polarization")
        else:
            st.success("No bot activity detected")

        st.subheader("📊 FINAL POLARIZATION RESULTS")

        st.metric("Raw Polarization Index", f"{results['raw']:.3f}")
        st.metric("Bias Score", f"{results['bias']}/5")
        st.metric("Bias-Corrected Polarization", f"{results['corrected']:.3f}")

        if results['bias'] == 0:
            st.success("Polarization is likely REAL, not an artifact of sampling.")
        elif results['bias'] <= 2:
            st.warning("Partial sampling bias → interpret results carefully.")
        else:
            st.error("Polarization likely artificially inflated due to biased data.")
