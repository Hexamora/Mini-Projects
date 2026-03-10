import requests

def detect_waf(url):
    print(f"[*] Menganalisis: {url}")
    
    # Header palsu agar terlihat seperti browser asli
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    try:
        # 1. Kirim request normal
        response = requests.get(url, headers=headers, timeout=10)
        
        # 2. Kirim request "mencurigakan" untuk memicu reaksi WAF (XSS payload)
        malicious_url = f"{url}?id=<script>alert('waf_test')</script>"
        attack_res = requests.get(malicious_url, headers=headers, timeout=10)
        
        all_headers = str(response.headers) + str(attack_res.headers)
        all_content = response.text + attack_res.text

        # Logika deteksi sederhana
        waf_signatures = {
            "Cloudflare": ["cloudflare", "__cfduid", "cf-ray"],
            "Imperva / Incapsula": ["incapsula", "visid_incap", "X-Iinfo"],
            "Akamai": ["akamai", "ak_bmsc", "akamai-ghost"],
            "AWS WAF": ["awselb", "aws-waf", "x-amz-id-2"],
            "ModSecurity": ["mod_security", "NOYB"],
            "F5 BIG-IP": ["BigIP", "TS", "F5"],
            "Sucuri": ["sucuri", "x-sucuri-id"]
        }

        found = False
        for waf_name, signatures in waf_signatures.items():
            for sig in signatures:
                if sig.lower() in all_headers.lower() or sig.lower() in all_content.lower():
                    print(f"[!] WAF Terdeteksi: {waf_name} (Signature: {sig})")
                    found = True
                    break
            if found: break
        
        if not found:
            print("[-] Tidak ada WAF populer yang terdeteksi.")

    except Exception as e:
        print(f"[X] Error: {e}")

# Contoh penggunaan
target = input("Masukkan url target anda: ") # Ganti dengan URL target
detect_waf(target)
