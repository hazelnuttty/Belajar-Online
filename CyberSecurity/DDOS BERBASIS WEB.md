# Panduan Serangan DDoS

## 📌 Apa Itu DDoS?
DDoS (Distributed Denial of Service) adalah serangan yang bertujuan untuk membuat layanan online tidak dapat diakses dengan membanjiri server target dengan lalu lintas berlebihan.

## 🔥 Jenis-Jenis Serangan DDoS

1. **Volumetric Attack** (Serangan Volume)
   - Menghabiskan bandwidth target dengan lalu lintas data yang besar.
   - Contoh: UDP Flood, ICMP Flood (Ping Flood), Amplification Attack.

2. **Protocol Attack** (Serangan Protokol)
   - Mengeksploitasi kelemahan dalam protokol jaringan.
   - Contoh: SYN Flood, Ping of Death, Smurf Attack.

3. **Application Layer Attack** (Serangan Lapisan Aplikasi)
   - Menargetkan aplikasi web dengan permintaan yang berlebihan.
   - Contoh: HTTP Flood, Slowloris, XML-RPC Attack.

## 🛠 Alat Untuk Menguji DDoS

1. **Low Orbit Ion Cannon (LOIC)**
   - Alat berbasis GUI untuk mengirimkan lalu lintas UDP, TCP, dan HTTP.

2. **High Orbit Ion Cannon (HOIC)**
   - Versi lebih kuat dari LOIC yang mampu melakukan serangan multi-threading.

3. **hping3**
   - Alat untuk mengirim paket yang dapat digunakan untuk simulasi DDoS.
   - Contoh perintah:
     ```sh
     hping3 -S -p 80 --flood --rand-source target.com
     ```

4. **GoldenEye**
   - HTTP DoS tool untuk serangan lapisan aplikasi.

## 🔐 Cara Mencegah Serangan DDoS

1. **Gunakan WAF (Web Application Firewall)**
   - Contoh: Cloudflare, AWS Shield.

2. **Batasi Traffic dengan Rate Limiting**
   - Konfigurasi pada Nginx:
     ```nginx
     limit_req_zone $binary_remote_addr zone=one:10m rate=5r/s;
     server {
         location / {
             limit_req zone=one burst=10 nodelay;
         }
     }
     ```

3. **Gunakan Load Balancer**
   - Sebarkan lalu lintas ke beberapa server untuk mengurangi beban.

4. **Aktifkan Captcha untuk Perlindungan HTTP Flood**
   - Contoh: Google reCAPTCHA.

5. **Gunakan CDN untuk Mengurangi Beban Server**
   - Contoh: Cloudflare, Akamai, Fastly.

## 🔗 Link Pengujian
Halo user, Kamu sudah siap untuk pengujian?, Kami sudah siapkan ddos berbasis web. Kamu akan mengddos web yang telah kita buat,
Ayo [klik](https://hazelnuttty.github.io/ddos-web-tes/) link pengujian sekarang

## 📢 Kesimpulan
DDoS adalah ancaman serius yang dapat menyebabkan layanan down dalam waktu singkat. Memahami cara kerja dan metode mitigasi sangat penting untuk melindungi sistem dari serangan ini.

---
**⚠️ Panduan ini hanya untuk edukasi! Jangan gunakan untuk aktivitas ilegal!**

