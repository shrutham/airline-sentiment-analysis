import streamlit as st
from src.predict import predict_sentiment

st.title("✈ Airline Sentiment Analyzer")

user_input = st.text_area(
    "Enter a tweet",
    placeholder="e.g., Flight was delayed but staff were helpful"
)
if st.button("Analyze"):
    if user_input.strip():
        result = predict_sentiment(user_input)
        st.success(f"Sentiment: {result}")
    else:
        st.warning("Please enter text")

st.caption("Note: Model may misclassify mixed sentiments (e.g., sentences with 'but') due to limited context understanding.")
