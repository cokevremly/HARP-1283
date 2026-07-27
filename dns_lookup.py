import dns.resolver
from urllib.parse import urlparse #url'i https'ten parse edip sadece domain.com kısmını almak için


def dns_lookup(url):
    domain = urlparse(url).netloc #url'i parse edip sadece domain.com kısmını almak için

    dns_info = {} #dictionary oluşturur. Toplanan her DNS kaydı buna eklenir

    record_types = [ #DNS kayıt türlerini liste olarak tanımlar
        'A', 
        'AAAA', 
        'MX', 
        'NS', 
        'CNAME', 
        'TXT'
    ] 

    for record in record_types:
        records = []

        try:
            answers = dns.resolver.resolve(domain, record) #Kayıtlar için DNS sorgusu yapar. ham cevaplardır

            for answer in answers:
                records.append(answer.to_text()) #cevapları listeye ekler. temiz veridir.

            dns_info[record] = records #her kayıt türü için dictionary'ye ekler

        except:
            dns_info[record] = [] #eğer kayıt yoksa boş liste ekler  

    return dns_info #dictionary döndürür. Örn: {'A': ['192.168.1.1']}






    a_records = [] #A kayıtları için liste oluşturur
    for answer in answers:
        a_records.append(answer.to_text()) #A kayıtlarını listeye ekler

    dns_info = {} #dictionary oluşturur

    #exception için:
    try:
        answers = dns.resolver.resolver(domain, 'A') #A kaydı için DNS sorgusu yapar
        dns_info['A_records'] = a_records #A kayıtlarını dictionary'ye ekler

    except:
        dns_info['A_records'] = [] #eğer A kaydı yoksa boş liste ekler
    

    return dns_info
