import json


with open("C:/Users/lenovo/OneDrive/Resimler/Masaüstü/veriler/etiketlenmis_yorumlar.json", "r", encoding="utf-8") as f:
    data = json.load(f)


with open("C:/Users/lenovo/OneDrive/Resimler/Masaüstü/veriler/etiketlenmis_yorumlar_line.json", "w", encoding="utf-8") as f:
    for entry in data:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")

