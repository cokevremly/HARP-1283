import os
import requests
from dotenv import load_dotenv

load_dotenv() #.env dosyasındaki API anahtarını pythona tanıtır.
API_KEY = os.getenv("ABUSEIPDB_API_KEY") #.env içindeki ABUSE_IPDB değerini alığ API_KEY değişkenine atar.
def check_ip(ip): #bu func ip adresini alıp abuseipdb de sorgulayacak
    url = "https://api.abuseipdb.com/api/v2/check" #abuseipdb ip sorgulama adresi
    headers = {
        "Key": API_KEY, #API anahtarı
        "Accept": "application/json" #cevabı json olarak alıyoruz
    }
    params = {
        "ipAddress": ip, #fonksiyona verdiğimiz ip adresi
        "maxAgeInDays": 90 #son 90 günlük veriyi dikkate al
    }
    response = requests.get(url, headers=headers, params=params) #IĞ sorgusunu abuseipdb ye gönderir ve cevabı response içine alır
    if response.status_code == 200:
        return response.json() #200, sorgu başarılı anlamına gelir ve cevabı json formatında döndürür
    return None #sorgu başarısız ise None döndürür














