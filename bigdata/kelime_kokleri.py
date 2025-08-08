import json
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer


nltk.download("punkt")
nltk.download("wordnet")


with open("C:/Users/lenovo/OneDrive/Resimler/Masaüstü/veriler/stopwords_temizlenmis.json", "r", encoding="utf-8") as f:
    data = json.load(f)

stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

def process_text(text):
    words = word_tokenize(text)
    stemmed_words = [stemmer.stem(word) for word in words]  
    lemmatized_words = [lemmatizer.lemmatize(word) for word in stemmed_words] 
    return " ".join(lemmatized_words)


processed_reviews = [{"film_id": d["film_id"], "author": d["author"], "content": process_text(d["content"])} for d in data]

with open("C:/Users/lenovo/OneDrive/Resimler/Masaüstü/veriler/kelime_kokleri.json", "w", encoding="utf-8") as f:
    json.dump(processed_reviews, f, ensure_ascii=False, indent=4)

print("Stemming ve Lemmatization işlemi tamamlandı, veri yeni dosyaya kaydedildi!")

