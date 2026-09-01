import os
from urllib import response
import requests
from dotenv import load_dotenv

load_dotenv() #.env dosyasındaki API anahtarını pythona tanıtır.
API_KEY = os.getenv("OTX_API_KEY") #.env içindeki OTX değerini alığ API_KEY değişkenine atar.
def check_ip_otx(ip): #bu func ip adresini alıp otx te sorgulayacak
    url = f"https://otx.alienvault.com/api/v1/indicators/IPv4/{ip}/general" #otx ip sorgulama adresi 
    headers = {
        "X-OTX-API-KEY": API_KEY, #API anahtarı
    }
    response = requests.get(url, headers=headers) #IP sorgusunu otx e gönderir ve cevabı response içine alır
    if response.status_code == 200:
        return response.json()

    print("Status Code:", response.status_code)
    print("Response:", response.text)
    return None
