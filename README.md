# Airline Sentiment Analysis

## Problem
Classify airline tweets into Positive, Neutral, Negative.

## Approach
- Text cleaning
- POS tagging & phrase extraction
- TF-IDF vectorization
- Logistic Regression model

## Features
- Sentiment prediction
- Phrase-based insights
- Streamlit web app

## Results
Accuracy: ~77%

## Run
pip install -r requirements.txt
streamlit run app.py

## Insights on Outputs
The model tends to classify mixed-sentiment sentences as negative due to the presence of strong negative keywords. This highlights a limitation of TF-IDF-based models, which do not capture contextual relationships such as contrast (e.g., "but").