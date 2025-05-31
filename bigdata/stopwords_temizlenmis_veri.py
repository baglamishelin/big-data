import json
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# NLTK veri setini indir (ilk defa çalıştırıyorsan)
import nltk

nltk.download('punkt')        # Cümle/parça ayırma aracı
nltk.download('punkt_tab')    # (Eksik olan veri bu!)
nltk.download('stopwords')    # Stop word listesi


# JSON dosyasını yükle
with open("C:/Users/lenovo/OneDrive/Resimler/Masaüstü/veriler/temizlenmis_yorumlar.json", "r", encoding="utf-8") as f:
    data = json.load(f)

stop_words = set(stopwords.words("english"))

def remove_stopwords(text):
    words = word_tokenize(text)
    filtered_words = [word for word in words if word.lower() not in stop_words]
    return " ".join(filtered_words)

# Yorumları stop words olmadan kaydet
filtered_reviews = [{"film_id": d["film_id"], "author": d["author"], "content": remove_stopwords(d["content"])} for d in data]

with open("C:/Users/lenovo/OneDrive/Resimler/Masaüstü/veriler/stopwords_temizlenmis.json", "w", encoding="utf-8") as f:
    json.dump(filtered_reviews, f, ensure_ascii=False, indent=4)

print("Stop words temizlendi ve veri yeni dosyaya kaydedildi!")
