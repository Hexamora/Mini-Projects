<div align="center">

```
██╗    ██╗ █████╗ ███████╗    ██████╗ ███████╗████████╗███████╗ ██████╗████████╗ ██████╗ ██████╗ 
██║    ██║██╔══██╗██╔════╝    ██╔══██╗██╔════╝╚══██╔══╝██╔════╝██╔════╝╚══██╔══╝██╔═══██╗██╔══██╗
██║ █╗ ██║███████║█████╗      ██║  ██║█████╗     ██║   █████╗  ██║        ██║   ██║   ██║██████╔╝
██║███╗██║██╔══██║██╔══╝      ██║  ██║██╔══╝     ██║   ██╔══╝  ██║        ██║   ██║   ██║██╔══██╗
╚███╔███╔╝██║  ██║██║         ██████╔╝███████╗   ██║   ███████╗╚██████╗   ██║   ╚██████╔╝██║  ██║
 ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝         ╚═════╝ ╚══════╝   ╚═╝   ╚══════╝ ╚═════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝
```

# 🛡️ WAF Detector

**Alat deteksi Web Application Firewall berbasis Python yang cepat dan ringan**

[![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)]()
[![Security](https://img.shields.io/badge/Purpose-Education%20Only-orange?style=for-the-badge)]()

> ⚡ Deteksi WAF populer hanya dengan satu perintah — cepat, akurat, tanpa fuss.

</div>

---

## 📌 Tentang

**WAF Detector** adalah tool berbasis Python yang dirancang untuk mengidentifikasi keberadaan *Web Application Firewall (WAF)* pada sebuah website target. Dengan mengirimkan request normal dan request "mencurigakan" (XSS payload), tool ini menganalisis respons header dan konten untuk mendeteksi fingerprint WAF yang dikenal.

> 🎓 **Disclaimer:** Tool ini dibuat **hanya untuk tujuan edukasi dan penetration testing yang sah**. Selalu dapatkan izin tertulis sebelum melakukan pengujian terhadap sistem milik orang lain.

---

## 🔍 WAF yang Dapat Dideteksi

| # | WAF | Signature yang Dicari |
|---|-----|-----------------------|
| 1 | ☁️ **Cloudflare** | `cloudflare`, `__cfduid`, `cf-ray` |
| 2 | 🔰 **Imperva / Incapsula** | `incapsula`, `visid_incap`, `X-Iinfo` |
| 3 | 🌐 **Akamai** | `akamai`, `ak_bmsc`, `akamai-ghost` |
| 4 | ☁️ **AWS WAF** | `awselb`, `aws-waf`, `x-amz-id-2` |
| 5 | 🔒 **ModSecurity** | `mod_security`, `NOYB` |
| 6 | ⚙️ **F5 BIG-IP** | `BigIP`, `TS`, `F5` |
| 7 | 🛡️ **Sucuri** | `sucuri`, `x-sucuri-id` |

---

## ⚙️ Cara Kerja

```
┌─────────────┐        ┌──────────────────┐        ┌─────────────────────┐
│  User Input │──URL──▶│  Request Normal  │──────▶ │  Analisis Header &  │
│   (Target)  │        └──────────────────┘        │  Response Content   │
└─────────────┘        ┌──────────────────┐        │                     │
                       │ Request XSS Test │──────▶ │  Pattern Matching   │
                       └──────────────────┘        └──────────┬──────────┘
                                                              │
                                          ┌───────────────────▼──────────────────┐
                                          │  [!] WAF Terdeteksi  /  [-] Tidak Ada │
                                          └──────────────────────────────────────┘
```

1. **Request Normal** — Mengirim HTTP GET dengan User-Agent browser asli
2. **Request Mencurigakan** — Menyisipkan XSS payload untuk memancing respons WAF
3. **Analisis Signature** — Membandingkan header & konten dengan database signature WAF
4. **Output Hasil** — Menampilkan WAF yang terdeteksi beserta signature yang cocok

---

## 🚀 Instalasi & Penggunaan

### Prasyarat

```bash
python --version   # Pastikan Python 3.x terinstall
```

### Install Dependensi

```bash
pip install requests
```

### Clone & Jalankan

```bash
# Clone repository
git clone https://github.com/username/waf-detector.git
cd waf-detector

# Jalankan tool
python waf_detector.py
```

### Contoh Output

```
Masukkan url target anda: https://example.com

[*] Menganalisis: https://example.com
[!] WAF Terdeteksi: Cloudflare (Signature: cf-ray)
```

```
Masukkan url target anda: https://another-site.com

[*] Menganalisis: https://another-site.com
[-] Tidak ada WAF populer yang terdeteksi.
```

---

## 📁 Struktur Project

```
waf-detector/
│
├── 📄 waf_detector.py     # Script utama
├── 📖 README.md           # Dokumentasi
└── 📜 LICENSE             # Lisensi MIT
```

---

## 🧩 Kode Utama

```python
import requests

def detect_waf(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)...'
    }
    
    # Kirim dua jenis request: normal & XSS payload
    response = requests.get(url, headers=headers, timeout=10)
    attack_res = requests.get(f"{url}?id=<script>alert('waf_test')</script>", ...)
    
    # Cocokkan dengan signature database
    waf_signatures = {
        "Cloudflare": ["cloudflare", "__cfduid", "cf-ray"],
        # ... dan lainnya
    }
```

---

## 🔧 Pengembangan Lanjutan

Beberapa ide untuk meningkatkan kemampuan tool ini:

- [ ] 📊 Tambah output format JSON / CSV
- [ ] 🔄 Support multiple URL sekaligus (bulk scan)
- [ ] 🌐 Integrasi proxy & Tor untuk anonimitas
- [ ] 📦 Perluas database signature WAF
- [ ] 🖥️ Buat tampilan CLI yang lebih interaktif (rich / colorama)
- [ ] 📡 Tambah deteksi berbasis respons status code (403, 406, 501)

---

## ⚠️ Legal & Etika

```
PERINGATAN PENTING
==================
Tool ini hanya boleh digunakan untuk:
  ✅ Pengujian terhadap sistem milik sendiri
  ✅ Bug bounty program yang sah
  ✅ Penetration testing dengan izin tertulis
  ✅ Tujuan edukasi dan riset keamanan

DILARANG KERAS:
  ❌ Menggunakan tool ini tanpa izin pemilik sistem
  ❌ Penggunaan untuk tujuan ilegal / kriminal

Penulis tidak bertanggung jawab atas penyalahgunaan tool ini.
```

---

## 📜 Lisensi

Didistribusikan di bawah **MIT License**. Lihat file `LICENSE` untuk detail lengkap.

---

<div align="center">

**Dibuat dengan ❤️ untuk komunitas keamanan siber Indonesia**

*"Knowledge is power — use it responsibly."*

⭐ Jangan lupa beri bintang kalau tool ini bermanfaat!

</div>
