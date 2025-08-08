import requests
import json

API_KEY = "6d8f12d9628ccac80921d9a99228498f"  
movie_ids = []


categories = ["popular", "top_rated", "upcoming", "now_playing"]

for category in categories:
    for page in range(1, 10): 
        url = f"https://api.themoviedb.org/3/movie/{category}?api_key={API_KEY}&language=en-US&page={page}"
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            ids = [movie["id"] for movie in data.get("results", [])]
            movie_ids.extend(ids)
        else:
            print(f"{category} kategorisi - Sayfa {page} için hata: {response.status_code}")


movie_ids = list(set(movie_ids))


with open("C:/Users/lenovo/OneDrive/Resimler/Masaüstü/veriler/film_id_listesi.json", "w", encoding="utf-8") as f:
    json.dump(movie_ids, f, ensure_ascii=False, indent=4)

print("Toplam film ID sayısı:", len(movie_ids))

