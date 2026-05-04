# Data cleaning
import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords

stop_words = set(stopwords.words('english'))


def clean_text(text):
    text = str(text).lower()
    text = re.sub(r'http\S+', '', text)        # remove links
    text = re.sub(r'@\w+', '', text)           # remove mentions
    text = re.sub(r'[^\w\s]', '', text)        # remove punctuation
    
    words = text.split()
    words = [w for w in words if w not in stop_words]
    
    return " ".join(words)