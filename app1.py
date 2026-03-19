import streamlit as st
from major_pro import run_bias_detector

st.set_page_config(page_title="Polarization Analyzer", layout="centered")

st.title("🔎 Political Polarization Bias Detector")

st.write("Enter multiple tweets (one per line)")

text_input = st.text_area(
    "Tweets",
    height=200,
    placeholder="Example:\nGovernment policies are destroying the economy\nThis election is unfair\nPoliticians are corrupt"
)

if st.button("Analyze"):

    if text_input.strip() == "":
        st.warning("Please enter at least one tweet.")
    else:
        tweets = [t.strip() for t in text_input.split("\n") if t.strip() != ""]

        results = run_bias_detector(tweets)

        st.write("## 🔎 Running Political Polarization Bias Detector...")

        # User Dominance
        st.write(f"👤 User Dominance Ratio: {results['user_dominance']:.3f}")
        if results['user_dominance'] < 0.3:
            st.success("No major echo chamber bias.")
        else:
            st.warning("Possible echo chamber bias detected.")

        # Topic Focus
        st.write(f"🗳 Political Topic Focus: {results['topic_focus']:.3f}")
        if results['topic_focus'] < 0.5:
            st.success("Topic distribution is not overly political.")
        else:
            st.warning("Dataset heavily political.")

        # Temporal Spike
        st.write(f"⏳ Temporal Spike Ratio: {results['temporal_spike']:.2f}")
        st.success("Stable timeline, no event-driven distortion.")

        # Sentiment Skew
        st.write(f"💢 Sentiment Skew: {results['sentiment_skew']:.3f}")
        if results['sentiment_skew'] < 0.5:
            st.success("Sentiment distribution is not highly skewed.")
        else:
            st.warning("High sentiment skew detected.")

        # Bot Detection
        st.write(f"🤖 Bot-like Users Detected: {results['bot_users']}")
        if results['bot_users'] > 0:
            st.warning("Potential automated accounts increasing polarization.")
        else:
            st.success("No bot activity detected.")

        # Final Results
        st.write("## 📊 FINAL POLARIZATION RESULTS")

        st.write(f"• Raw Polarization Index: {results['raw']:.3f}")
        st.write(f"• Bias Score: {results['bias']}/5")
        st.write(f"• Bias-Corrected Polarization: {results['corrected']:.3f}")

        if results['bias'] == 0:
            st.success("Polarization is likely REAL, not an artifact of sampling.")
        elif results['bias'] <= 2:
            st.warning("Partial sampling bias → interpret results carefully.")
        else:
            st.error("Polarization likely artificially inflated due to biased data.")
