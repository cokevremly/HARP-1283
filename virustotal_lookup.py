import requests #API'ye istek göndermek için
import base64 #URL'yi base64 formatına çevirmek için
import os # API key'i environment variable'dan almak için
from dotenv import load_dotenv #.env dosyasını okuyup environment variable olarak yüklemek için

load_dotenv() # .env dosyasını yükler. env dosyasını .gitignore dosyasına eklemeliyiz ki github'a yüklenmesin. API key gizli kalmalı.
#.env dosyasını gitignore dosyasına ekleyeceğiz.

API_KEY = os.getenv("VIRUSTOTAL_API_KEY") # Get the API key from environment variable

if not API_KEY:
    raise ValueError("VIRUSTOTAL_API_KEY environment variable not set. Please set it in your .env file.")

def virustotal_lookup(url):

    url_id = base64.urlsafe_b64encode(url.encode()).decode().strip("=") 
    #url.encode(), string olan url'yi byte formatına çevirir.
    #base64.urlsafe_b64encode() fonksiyonu, byte formatındaki url'yi base64 formatına çevirir.
    #decode() fonksiyonu, byte formatındaki base64'ü tekrar string formatına çevirir.
    #strip("=") fonksiyonu, base64 formatındaki stringin sonundaki '=' karakterlerini temizler. Çünkü virustotal API'si url_id'yi '=' karakterleri olmadan istiyor.

    headers = {
        "x-apikey": API_KEY
    } # API istekleri için gerekli header bilgisi. API key'i header'da gönderiyoruz.

    api_url = f"https://www.virustotal.com/api/v3/urls/{url_id}" # Virustotal API'sine istek atacağımız URL.

    response = requests.get(api_url, headers=headers) # API'ye GET isteği gönderiyoruz. response değişkeni, API'den gelen cevabı tutar.

    if response.status_code == 200: # API isteği başarılı ise 
        data = response.json() # API'den gelen cevabı JSON formatında alıyoruz. data değişkeni, API'den gelen cevabı tutar.

        attributes = data.get("data", {}).get("attributes", {}) # API cevabındaki "data" ve "attributes" alanlarını alıyoruz. Eğer bu alanlar yoksa boş dictionary döndürür.

        stats = attributes.get("last_analysis_stats", {}) # API cevabındaki "last_analysis_stats" alanını alıyoruz. Eğer bu alan yoksa boş dictionary döndürür.

        virustotal_info = {
            "Malicious": stats.get("malicious", 0), # "malicious" alanını alıyoruz. Eğer bu alan yoksa 0 döndürür.
            "Suspicious": stats.get("suspicious", 0), # "suspicious" alanını alıyoruz. Eğer bu alan yoksa 0 döndürür.
            "Harmless": stats.get("harmless", 0), # "harmless" alanını alıyoruz. Eğer bu alan yoksa 0 döndürür.
            "Undetected": stats.get("undetected", 0), # "undetected" alanını alıyoruz. Eğer bu alan yoksa 0 döndürür.
            "Reputation": stats.get("reputation", 0), # # Reputation score, domain'in geçmiş güvenilirlik durumunu gösteren VirusTotal itibar puanıdır.
        }
        return virustotal_info # virustotal_info dictionary'sini döndürüyoruz. Örn: {'malicious': 0, 'suspicious': 0, 'harmless': 70, 'undetected': 0}
    
    else:
        return {
            "error": f"VirusTotal API error: {response.status_code}",
            "message": response.text

        }