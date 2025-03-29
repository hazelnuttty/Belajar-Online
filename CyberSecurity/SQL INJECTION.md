# Panduan SQL Injection

## 📌 Apa Itu SQL Injection?
SQL Injection (SQLi) adalah teknik serangan yang mengeksploitasi celah keamanan pada input aplikasi yang berinteraksi dengan database SQL. Penyerang dapat menyisipkan atau memodifikasi query SQL untuk mendapatkan, mengubah, atau menghapus data tanpa otorisasi.

## 🔥 Jenis-Jenis SQL Injection

1. **Union-Based SQL Injection**
   - Memanfaatkan perintah `UNION SELECT` untuk mengambil data dari tabel lain.
   - Contoh Payload:
     ```sql
     ' UNION SELECT username, password FROM users --
     ```

2. **Error-Based SQL Injection**
   - Memicu error untuk mendapatkan informasi struktur database.
   - Contoh Payload:
     ```sql
     ' OR 1=1 ORDER BY 100 --
     ```

3. **Blind SQL Injection**
   - Serangan dilakukan dengan menganalisis respons aplikasi, biasanya berupa `true/false`.
   - Contoh Payload:
     ```sql
     ' AND (SELECT COUNT(*) FROM users) > 0 --
     ```

4. **Time-Based SQL Injection**
   - Mengeksekusi query yang memperlambat respons untuk mendapatkan informasi.
   - Contoh Payload:
     ```sql
     ' OR IF(1=1, SLEEP(5), 0) --
     ```

## 🔗 LinknPengujian
Kalian sudah tau kan cara memakai `SQL INJECTION`, Saya akan mengetes kalian untuk melakukan sql injetion
simple menggunakan `Eror-Based SQL Injetion`, [UJIAN SQL INJECTION](https://sql-tes.netlify.app/), Klik untuk memulai tes

## 🔧 Cara Mengidentifikasi Celah SQL Injection
1. Masukkan karakter `'` atau `"` dalam input dan lihat apakah ada error.
2. Coba gunakan `OR 1=1` dan periksa apakah hasil berubah.
3. Gunakan `ORDER BY` dengan angka besar untuk melihat jumlah kolom tabel.

## 🔐 Cara Mencegah SQL Injection
1. **Gunakan Parameterized Query**
   ```python
   cursor.execute("SELECT * FROM users WHERE username = ?", (user_input,))
   ```

2. **Gunakan ORM (Object-Relational Mapping)**
   - Contoh pada SQLAlchemy:
     ```python
     user = session.query(User).filter_by(username=user_input).first()
     ```

3. **Batasi Hak Akses Database**
   - Gunakan akun database dengan izin terbatas.

4. **Gunakan Web Application Firewall (WAF)**
   - Contoh WAF: ModSecurity, Cloudflare.

## 🛠 Alat Untuk Menguji SQL Injection
- **SQLmap** (Otomatisasi eksploitasi SQL Injection)
- **Burp Suite** (Intercept dan modifikasi request)
- **Havij** (GUI untuk eksploitasi SQLi)

## 📢 Kesimpulan
SQL Injection adalah ancaman serius yang dapat menyebabkan kebocoran data besar-besaran. Dengan menerapkan teknik keamanan yang tepat, serangan ini dapat dicegah secara efektif.

---
**⚠️ Gunakan informasi ini dengan bijak! Semua bentuk pengujian harus dilakukan pada sistem yang diizinkan.**

