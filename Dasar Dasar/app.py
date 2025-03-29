# Materi Dasar Flask untuk Pemula

## 1. Apa itu Flask?
Flask adalah framework web berbasis Python yang ringan dan mudah digunakan untuk membuat aplikasi web.

## 2. Instalasi Flask
Gunakan perintah berikut untuk menginstal Flask:
```bash
pip install flask
```

## 3. Membuat Aplikasi Flask Pertama
Buat file `app.py` dan tulis kode berikut:
```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask!"

if __name__ == '__main__':
    app.run(debug=True)
```
Jalankan dengan perintah:
```bash
python app.py
```
Lalu buka browser dan akses `http://127.0.0.1:5000/`.

## 4. Routing di Flask
Tambahkan route lain untuk halaman baru:
```python
@app.route('/about')
def about():
    return "Halaman Tentang Kami"
```

## 5. Menggunakan Template HTML
Buat folder `templates` dan file `index.html` di dalamnya:
```html
<!DOCTYPE html>
<html>
<head>
    <title>Flask App</title>
</head>
<body>
    <h1>Selamat Datang di Flask!</h1>
</body>
</html>
```
Lalu ubah `app.py`:
```python
from flask import render_template

@app.route('/')
def home():
    return render_template('index.html')
```

## 6. Menggunakan Form dan Request
Tambahkan form HTML ke `index.html`:
```html
<form action="/submit" method="post">
    <input type="text" name="nama" placeholder="Masukkan nama">
    <input type="submit" value="Kirim">
</form>
```
Tambahkan kode di `app.py` untuk menangani form:
```python
from flask import request

@app.route('/submit', methods=['POST'])
def submit():
    nama = request.form['nama']
    return f"Halo, {nama}!"
```

## 7. Kesimpulan
Flask adalah framework sederhana untuk membangun aplikasi web dengan Python. Dengan memahami dasar-dasar ini, Anda bisa mulai mengembangkan aplikasi web sendiri!

