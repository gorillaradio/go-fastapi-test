import nltk
from nltk.corpus import stopwords
from collections import Counter
import json

# Scarica le stopwords italiane (eseguire solo la prima volta)
nltk.download('stopwords')

# Funzione per rimuovere le stopwords italiane
def remove_stopwords(text):
    stop_words = set(stopwords.words('italian'))
    words = text.split()
    filtered_text = [word for word in words if word.lower() not in stop_words]
    return " ".join(filtered_text)

# Funzione per trovare le n parole più frequenti
def most_frequent_words(text, n=10):
    words = text.split()
    frequency = Counter(words)
    most_common = frequency.most_common(n)
    return [word for word, _ in most_common]

# Funzione per trasformare un array in JSON
def array_to_json(array):
    return json.dumps(array, ensure_ascii=False)