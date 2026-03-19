import streamlit as st
from major_pro import run_bias_detector

# Page setup
st.set_page_config(page_title="Polarization Analyzer", layout="centered")

st.title("🔎 Political Polarization Bias Detector")

st.write("Enter multiple tweets (one per line)")

# Input box
text_input = st.text_area(
    "Tweets",
    height=200,
    placeholder="Example:\nGovernment policies are destroying the economy\nThis election is unfair\nPoliticians are corrupt"
)

# Button
if st.button("Analyze"):

    if text_input.strip() == "":
        st.warning("Please enter at least one tweet.")
    else:
        # Convert input into list
        tweets = [t.strip() for t in text_input.split("\n") if t.strip() != ""]

        # Call your project function
        results = run_bias_detector(tweets)

        st.write("## 🔎 Running Political Polarization Bias Detector...")

        # Metrics
        st.write(f"👤 User Dominance Ratio: {results['user_dominance']:.3f}")
        st.write(f"🗳 Political Topic Focus: {results['topic_focus']:.3f}")
        st.write(f"⏳ Temporal Spike Ratio: {results['temporal_spike']:.2f}")
        st.write(f"💢 Sentiment Skew: {results['sentiment_skew']:.3f}")
        st.write(f"🤖 Bot-like Users Detected: {results['bot_users']}")

        # Final results
        st.write("## 📊 FINAL POLARIZATION RESULTS")

        st.write(f"• Raw Polarization Index: {results['raw']:.3f}")
        st.write(f"• Bias Score: {results['bias']}/5")
        st.write(f"• Bias-Corrected Polarization: {results['corrected']:.3f}")

        # Interpretation
        if results['bias'] == 0:
            st.success("Polarization is likely REAL, not an artifact of sampling.")
        elif results['bias'] <= 2:
            st.warning("Partial sampling bias → interpret results carefully.")
        else:
            st.error("Polarization likely artificially inflated due to biased data.")
