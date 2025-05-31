import json
import re

# JSON dosyasını yükle
with open("C:/Users/lenovo/OneDrive/Resimler/Masaüstü/veriler/film_yorumlari.json", "r", encoding="utf-8") as f:
    data = json.load(f)

def clean_text(text):
    text = re.sub(r'<.*?>', '', text)  # HTML etiketlerini kaldır
    text = re.sub(r'\W', ' ', text)  # Özel karakterleri kaldır
    return text.lower()

# Temizlenmiş veriyi kaydet
cleaned_reviews = [{"film_id": d["film_id"], "author": d["author"], "content": clean_text(d["content"])} for d in data]

with open("C:/Users/lenovo/OneDrive/Resimler/Masaüstü/veriler/temizlenmis_yorumlar.json", "w", encoding="utf-8") as f:
    json.dump(cleaned_reviews, f, ensure_ascii=False, indent=4)

print("Veri başarıyla temizlendi ve yeni dosyaya kaydedildi!")
