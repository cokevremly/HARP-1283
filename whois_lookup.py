import whois
from urllib.parse import urlparse


def normalize_date(date):
    if isinstance(date, list): #date bir liste mi diye kontrol eder.
        return date[0] #liste ise ilk eleman olan tarih bilgisini döndürür
    return date #date bir liste değilse olduğu gibi döndürür

def get_whois_info(url):

    domain = urlparse(url).netloc # (ENCAPSULATION)
    #girilen url i parse eder ve domaini ceker

    try:
        info = whois.whois(domain) #domainin whois bilgilerini getirir

        whois_data = { #whois kütüphanesinden şimdilik lazim olan verileri cektigimiz bir dictionary olusturduk
            "domain": domain,
            "registrar": info.registrar,
            "creation_date": normalize_date(info.creation_date),
            "updated_date": normalize_date(info.updated_date), #son guncelleme tarihi
            "expiration_date": normalize_date(info.expiration_date),
            "name_servers": info.name_servers,
            "status": info.status,
            "dnssec": info.dnssec,
        }
    except Exception as e:
        print(f"\nWHOIS lookup failed: {e}")

        whois_data = {
            "domain": domain,
            "registrar": None,
            "creation_date": None,
            "updated_date": None,
            "expiration_date": None,
            "name_servers": None,
            "status": None,
            "dnssec": None,
        }
    return whois_data    

    #{} ibaresi varsa dictionary, 
    # [] ibaresi varsa liste. 
    # ama ['...'] gibi bir string durumu varsa bu da dictionary
    
