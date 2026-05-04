import pickle
from src.preprocess import clean_text

model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

label_map = {0: "Negative", 1: "Neutral", 2: "Positive"}

def predict_sentiment(text):
    text = clean_text(text)
    vec = vectorizer.transform([text])
    pred = model.predict(vec)[0]
    return label_map[pred]