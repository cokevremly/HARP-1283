# 🛡️ HARP-1283

### Hybrid Analysis & Reconnaissance Platform v1.0

[for English](README-EN.md)

HARP-1283; **URL güvenlik analizi, risk skorlama, SSL/TLS incelemesi, domain istihbaratı, DNS analizi ve harici Threat Intelligence kaynaklarını** tek bir analiz akışında birleştiren Python tabanlı bir siber güvenlik platformudur.

Proje, şüpheli URL ve domainlerin güvenlik açısından incelenebilmesini sağlayan pratik ve geliştirilebilir bir platform olarak tasarlanmıştır.

> **1283** sayısı, Gazi Mustafa Kemal Atatürk'ün Kara Harp Okulu'ndaki öğrenci numarasından esinlenilmiştir.

---

## ✨ Özellikler

### 🔍 URL Güvenlik Analizi

HARP-1283, girilen URL'ler üzerinde kural tabanlı güvenlik analizi gerçekleştirir.

Mevcut kontroller:

* HTTPS kontrolü
* Şüpheli anahtar kelime tespiti
* Uzun URL tespiti
* Güvenlik bulgularının oluşturulması
* Risk skoru hesaplama
* Risk seviyesi sınıflandırması

Risk seviyeleri:

* 🟢 **LOW — Düşük**
* 🟡 **MEDIUM — Orta**
* 🔴 **HIGH — Yüksek**

---

### 🔐 SSL/TLS Analizi

Platform, hedef domain ile ilişkili SSL/TLS sertifikasını analiz eder.

İncelenebilen bilgiler:

* Sertifika sağlayıcısı
* Domain bilgileri
* Sertifika geçerliliği
* Kalan geçerlilik süresi

---

### 🌐 WHOIS Sorgulama

HARP-1283, hedef domain hakkında WHOIS bilgilerini alarak ek domain istihbaratı sağlar.

---

### 📡 DNS Analizi

Platform aşağıdaki yaygın DNS kayıt türlerini sorgulayabilir:

* A
* AAAA
* MX
* NS
* CNAME
* TXT

Bu bilgiler hedef domainin DNS altyapısı hakkında ek bağlam sağlar.

---

### 🦠 VirusTotal Entegrasyonu

HARP-1283, URL ve IP analizlerini harici tehdit istihbaratı verileriyle zenginleştirmek amacıyla VirusTotal entegrasyonu kullanır.

Alınabilen bilgiler arasında:

* Malicious tespitleri
* Suspicious tespitleri
* Harmless sonuçları
* Undetected sonuçları
* Reputation bilgisi

bulunur.

---

### 🚨 AbuseIPDB Entegrasyonu

Hedef ile ilişkili IP adresinin incelenmesinde AbuseIPDB verilerinden yararlanılabilir.

İlgili bilgiler:

* Kötüye Kullanım Güven Skoru (Abuse Confidence Score)
* Rapor sayısı
* Ülke
* ISP / organizasyon

---

### 🛰️ AlienVault OTX Entegrasyonu

AlienVault Open Threat Exchange (OTX), ek bir tehdit istihbaratı kaynağı olarak kullanılmaktadır.

Entegrasyon kapsamında:

* Güvenilirlik (Reputation)
* Tehidt itibarı kaydı sayısı (Pulse Count)
* Ülke
* ASN
* Organizasyon

gibi bilgiler alınabilir.

---

## 📊 Risk Skorlama

HARP-1283, güvenlik bulgularını ve mevcut tehdit istihbaratı sonuçlarını birleştirerek genel bir risk skoru hesaplar.

Örnek:

```text
Risk Score: 45/100
Risk Level: MEDIUM
```

Nihai skor, URL'nin özelliklerine ve mevcut tehdit istihbaratı sonuçlarına göre değişebilir.

---

## 📄 Güvenlik Raporlama

Analiz sonuçları tek bir güvenlik raporunda birleştirilir.

Rapor kapsamında:

* URL analiz bulguları
* Teknik bilgiler
* Tehdit istihbaratı sonuçları
* Risk skoru
* Risk seviyesi

sunulabilir.

Raporlama katmanı, gerçekleştirilen analizlerin kısa ve anlaşılır bir özetini oluşturmayı amaçlar.

---

## 🖥️ Web Arayüzü

HARP-1283, **Streamlit tabanlı bir web arayüzüne** sahiptir.

Arayüz üzerinden kullanıcı:

1. URL girebilir
2. Analizi başlatabilir
3. Güvenlik bulgularını inceleyebilir
4. SSL/TLS bilgilerini görüntüleyebilir
5. WHOIS ve DNS verilerini inceleyebilir
6. Tehdit İstihbaratı sonuçlarını görüntüleyebilir
7. Risk skorunu değerlendirebilir

---

## 🏗️ Proje Yapısı

```text
HARP-1283/
│
├── app.py                    # Streamlit web arayüzü
├── main.py                   # CLI giriş noktası
│
├── analyzer.py               # URL güvenlik analizi
├── scorer.py                 # Risk skoru hesaplama
├── report.py                 # Güvenlik raporu oluşturma
│
├── ssl_lookup.py             # SSL/TLS analizi
├── whois_lookup.py           # WHOIS sorgulama
├── dns_lookup.py             # DNS analizi
│
├── virustotal_lookup.py      # VirusTotal entegrasyonu
├── abuseipdb_lookup.py       # AbuseIPDB entegrasyonu
├── otx_lookup.py             # AlienVault OTX entegrasyonu
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🚀 Kurulum

Repoyu klonlayın:

```bash
git clone https://github.com/cokevremly/HARP-1283.git
```

Proje klasörüne girin:

```bash
cd HARP-1283
```

Gerekli paketleri yükleyin:

```bash
pip install -r requirements.txt
```

---

## ▶️ HARP-1283'ü Çalıştırma

### Streamlit Arayüzü

Aşağıdaki komutu çalıştırın:

```bash
streamlit run app.py
```

Uygulama varsayılan olarak:

```text
http://localhost:8501
```

adresinde açılır.

### CLI

Proje CLI üzerinden de çalıştırılabilir:

```bash
python main.py
```

---

## 🔑 API Yapılandırması

Bazı Threat Intelligence entegrasyonları API anahtarı gerektirir.

Desteklenen harici servisler:

* VirusTotal
* AbuseIPDB
* AlienVault OTX

API anahtarları **kod içerisinde tutulmamalı ve GitHub'a yüklenmemelidir.**

API anahtarlarının environment variable veya güvenli başka bir yapılandırma yöntemiyle saklanması önerilir.

---

## 🧪 Örnek Analiz

Bir URL Streamlit arayüzü veya CLI üzerinden analiz edilebilir.

Örnek bulgular:

```text
Findings:
- No HTTPS
- Login keyword detected
- Long URL detected

Risk Score: 45/100
Risk Level: MEDIUM
```

İlgili servisler kullanılabilir durumdaysa Threat Intelligence sonuçları da analize dahil edilir.

---

## 🛠️ Kullanılan Teknolojiler

* Python
* Streamlit
* SSL/TLS
* WHOIS
* DNS
* VirusTotal API
* AbuseIPDB API
* AlienVault OTX API
* Git
* GitHub

---

## 🗺️ Yol Haritası

HARP-1283 aktif geliştirme aşamasındadır.

Planlanan özellikler:

### 🔎 OSINT Modülü

### 🦠 Malware Analysis

### 🤖 AI Analyst

### 📡 Ek Threat Intelligence Kaynakları



## ⚠️ Uyarı

HARP-1283; **eğitim, araştırma ve yetkili güvenlik testleri** amacıyla geliştirilmiştir.

Yalnızca sahibi olduğunuz veya analiz etmek için açıkça yetkilendirildiğiniz URL, domain, IP adresi ve sistemleri analiz edilmelidir.

Projenin yetkisiz veya yasa dışı kullanımından geliştirici sorumlu değildir.

---

## 👩‍💻 Geliştirici

**Merve KOÇ**

https://www.linkedin.com/in/merve-ko%C3%A7-167194177/

---

