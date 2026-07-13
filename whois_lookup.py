import whois
from urllib.parse import urlparse


def get_whois_info(url):
    domain = urlparse(url).netloc # (ENCAPSULATION) 
    #girilen url i parse eder ve domaini ceker

    info = whois.whois(domain) #domainin whois bilgilerini getirir

    whois_data = { #whois kütüphanesinden şimdilik lazim olan verileri cektigimiz bir dictionary olusturduk
        "registrar": info.registrar,
        "creation_date": info.creation_date,
        "expiration_date": info.expiration_date,
    }
    #{} ibaresi varsa dictionary, 
    # [] ibaresi varsa liste. 
    # ama ['...'] gibi bir string durumu varsa bu da dictionary
    
    
    
    return whois_data

