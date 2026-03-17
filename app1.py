import streamlit as st
from major_pro import run_bias_detector

st.title("Political Polarization Bias Detector")

tweet = st.text_area("Enter Tweet or Text")

if st.button("Analyze"):

    results = run_bias_detector(tweet)

    raw = results["raw_polarization"]
    bias = results["bias_score"]
    corrected = raw / (1 + bias)

    st.subheader("🔎 Running Political Polarization Bias Detector")

    st.write(f"👤 User Dominance Ratio: {results['user_dominance']}")
    st.write(f"🗳 Political Topic Focus: {results['topic_focus']}")
    st.write(f"⏳ Temporal Spike Ratio: {results['temporal_spike']}")
    st.write(f"💢 Sentiment Skew: {results['sentiment_skew']}")
    st.write(f"🤖 Bot-like Users Detected: {results['bot_users']}")

    st.subheader("📊 FINAL POLARIZATION RESULTS")

    st.metric("Raw Polarization Index", f"{raw:.3f}")
    st.metric("Bias Score", f"{bias}/5")
    st.metric("Bias-Corrected Polarization", f"{corrected:.3f}")

    if bias == 0:
        st.success("Polarization is likely REAL, not an artifact of sampling.")
    elif bias <= 2:
        st.warning("Partial sampling bias → interpret results carefully.")
    else:
        st.error("Polarization is likely artificially inflated due to biased data.")
