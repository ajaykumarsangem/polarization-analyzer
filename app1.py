import streamlit as st
from major_pro import run_bias_detector

st.title("🔎 Political Polarization Analyzer")

text_input = st.text_area(
    "Enter Tweets (one per line)",
    height=200
)

if st.button("Analyze"):

    tweets = text_input.split("\n")

    results = run_bias_detector(tweets)

    st.write("### 🔎 Running Political Polarization Bias Detector")

    st.write(f"💢 Sentiment Skew: {results['sentiment_skew']:.3f}")

    st.write(f"🤖 Bot-like Users Detected: {results['bot_users']}")

    st.write("## 📊 FINAL POLARIZATION RESULTS")

    st.write(f"• Raw Polarization Index: {results['raw']:.3f}")
    st.write(f"• Bias Score: {results['bias']}/5")
    st.write(f"• Bias-Corrected Polarization: {results['corrected']:.3f}")
