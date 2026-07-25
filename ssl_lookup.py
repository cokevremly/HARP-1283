import socket
import ssl
from urllib.parse import urlparse #url'i https'ten parse edip sadece domain.com kısmını almak için
from datetime import datetime, UTC

def parse_certificate_section(section): #verilen sertifika bölümünü (issuer veya subject) bir sözlüğe dönüştürür

    data = {}

    for item in section:
        key = item[0][0]
        value = item[0][1]
        data[key] = value

    return data


def get_ssl_info(url):

    domain = urlparse(url).netloc #url'i parse edip sadece domain.com kısmını almak için

    sock = socket.create_connection((domain, 443)) #ssl sertifikası için 443 portuna bağlanılır.
    #ayrıca ilk yapmamız geken buydu yani socket ile önce bağlantı sağlamak
    #yukarıdaki satır normal bir TCP bağlantısı kurar. SSL sertifikası için bu bağlantıyı kullanacağız.
    
    context = ssl.create_default_context()
    #context: SSL bağlantısının ayarları ve kurallarıdır.

    secure_sock = context.wrap_socket(
        sock, 
        server_hostname=domain)
    #wrap_socket: yukarıdaki tcp bağlantısının üstüne ssl/tls protokolünü uyguluyor
    #yani socket bağlantısını daha güvenli hale getiriyor.
    #ayrıca secure_sock ssl bağlantısını temsil ediyor.

    certificate = secure_sock.getpeercert()
    # peer: karşı taraf demek, yukarıdaki satır karşı tarafın sertifikasını getirir.
    
    issuer = parse_certificate_section(certificate.get("issuer", [])) #dictionary olarak sertifikanın issuer kısmını alır
    subject = parse_certificate_section(certificate.get("subject", []))# dictionary olarak sertifikanın subject kısmını alır 

    expiry_date = datetime.strptime(
        certificate.get("notAfter"),
        "%b %d %H:%M:%S %Y GMT"
    ).replace(tzinfo=UTC) #sertifikanın geçerlilik bitiş tarihini datetime objesine çevirir ve UTC timezone ekler

    today = datetime.now(UTC) #bugünün tarihini UTC timezone ile alır

    days_remaining = (expiry_date - today).days #sertifikanın geçerlilik bitiş tarihi ile bugünün tarihini çıkarır ve kalan gün sayısını alır


    ssl_info = { #dictionary
        "issuer": issuer.get("organizationName"),
        "issued_to": subject.get("commonName"),
        "valid_from": certificate.get("notBefore"),
        "valid_until": certificate.get("notAfter"),
        "days_remaining": days_remaining,
    }

    secure_sock.close() #close() metodu ile secure_sock bağlantısını kapatır. Bu, kaynakları serbest bırakmak ve bağlantıyı düzgün bir şekilde sonlandırmak için önemlidir.
    sock.close() #close() metodu ile sock bağlantısını kapatır.


    return ssl_info

    