# Materi Dasar HTML untuk Pemula

## 1. Pengertian HTML
HTML (HyperText Markup Language) adalah bahasa markup yang digunakan untuk membuat halaman web. HTML terdiri dari elemen-elemen yang membentuk struktur sebuah website.

## 2. Struktur Dasar HTML
Setiap dokumen HTML memiliki struktur dasar seperti berikut:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Judul Halaman</title>
</head>
<body>
    <h1>Selamat Datang di HTML</h1>
    <p>Ini adalah paragraf pertama dalam HTML.</p>
</body>
</html>
```

## 3. Elemen Dasar HTML
### a. Heading (Judul)
Digunakan untuk membuat judul dalam halaman web. Ada enam tingkatan heading:
```html
<h1>Heading 1</h1>
<h2>Heading 2</h2>
<h3>Heading 3</h3>
<h4>Heading 4</h4>
<h5>Heading 5</h5>
<h6>Heading 6</h6>
```

### b. Paragraf
Digunakan untuk menulis teks dalam bentuk paragraf:
```html
<p>Ini adalah contoh paragraf.</p>
```

### c. Link (Tautan)
Digunakan untuk menautkan halaman web lain:
```html
<a href="https://www.google.com">Kunjungi Google</a>
```

### d. Gambar
Digunakan untuk menampilkan gambar dalam halaman web:
```html
<img src="gambar.jpg" alt="Deskripsi Gambar">
```

### e. Daftar
- **Daftar Tak Berurutan (Unordered List)**:
```html
<ul>
    <li>Item 1</li>
    <li>Item 2</li>
    <li>Item 3</li>
</ul>
```
- **Daftar Berurutan (Ordered List)**:
```html
<ol>
    <li>Item 1</li>
    <li>Item 2</li>
    <li>Item 3</li>
</ol>
```

### f. Tabel
Digunakan untuk menampilkan data dalam bentuk tabel:
```html
<table border="1">
    <tr>
        <th>Nama</th>
        <th>Usia</th>
    </tr>
    <tr>
        <td>Rerey</td>
        <td>20</td>
    </tr>
</table>
```

### g. Formulir
Digunakan untuk menerima input dari pengguna:
```html
<form action="submit.php" method="post">
    <label for="nama">Nama:</label>
    <input type="text" id="nama" name="nama">
    <br>
    <label for="email">Email:</label>
    <input type="email" id="email" name="email">
    <br>
    <input type="submit" value="Kirim">
</form>
```

## 4. Kesimpulan
HTML adalah dasar dari pembuatan halaman web. Dengan memahami elemen-elemen dasar ini, Anda bisa mulai membangun website sederhana. Untuk lebih lanjut, Anda bisa mempelajari CSS dan JavaScript untuk mempercantik dan menambah interaksi pada halaman web Anda.

