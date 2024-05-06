from flask import Flask, request, render_template
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import WordNetLemmatizer
from rank_bm25 import BM25Okapi
import pandas as pd

app = Flask(__name__)

# Ensure resources are downloaded
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Initialize lemmatizer and stop words
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

def tokenize_and_lemmatize(text):
    return [lemmatizer.lemmatize(word) for word in word_tokenize(text.lower()) if word.isalpha() and word not in stop_words]

# Example data frame (you will need to load your actual data here)
df = pd.read_json("ceo-letters.jsonl", lines=True)
texts = df['text'].tolist()
corpus = [tokenize_and_lemmatize(text) for text in texts]

bm25 = BM25Okapi(corpus)

def truncate_to_full_sentences(text, max_char_length):
    sentences = sent_tokenize(text)
    truncated_text = ""
    for sentence in sentences:
        if len(truncated_text) + len(sentence) <= max_char_length:
            truncated_text += sentence + " "
        else:
            break
    return truncated_text.strip()

def bm25_query2(query, top_n=5, max_char_length=400):
    tokenized_query = tokenize_and_lemmatize(query)
    scores = bm25.get_scores(tokenized_query)
    top_indexes = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)[:top_n]
    return [(truncate_to_full_sentences(texts[i], max_char_length), scores[i]) for i in top_indexes]

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        query = request.form.get("query")
        results = bm25_query2(query, top_n=1, max_char_length=200)  # Get only the top result
        top_result = results[0][0] if results else "No results found."  # Ensure we have results and get the first snippet
        return render_template("results.html", query=query, result=top_result)
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
