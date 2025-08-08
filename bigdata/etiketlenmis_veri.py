import json
from textblob import TextBlob


with open("C:/Users/lenovo/OneDrive/Resimler/Masaüstü/veriler/kelime_kokleri.json", "r", encoding="utf-8") as f:
    data = json.load(f)

def get_sentiment(text):
    sentiment_score = TextBlob(text).sentiment.polarity
    return "İyi" if sentiment_score > 0 else "Kötü"


labeled_reviews = [{"film_id": d["film_id"], "author": d["author"], "content": d["content"], "sentiment": get_sentiment(d["content"])} for d in data]

with open("C:/Users/lenovo/OneDrive/Resimler/Masaüstü/veriler/etiketlenmis_yorumlar.json", "w", encoding="utf-8") as f:
    json.dump(labeled_reviews, f, ensure_ascii=False, indent=4)

print("Yorumlar başarıyla etiketlendi ve yeni dosyaya kaydedildi!")

