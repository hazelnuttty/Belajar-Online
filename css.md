# Materi Dasar CSS untuk Pemula

## 1. Pengertian CSS
CSS (Cascading Style Sheets) adalah bahasa yang digunakan untuk mengatur tampilan dan desain elemen dalam HTML. Dengan CSS, kita bisa mengubah warna, ukuran, tata letak, dan animasi halaman web.

## 2. Cara Menggunakan CSS
Ada tiga cara menggunakan CSS:

### a. Inline CSS (Langsung di dalam tag HTML)
```html
<p style="color: blue; font-size: 20px;">Ini adalah paragraf berwarna biru.</p>
```

### b. Internal CSS (Dalam tag `<style>` di dalam file HTML)
```html
<!DOCTYPE html>
<html>
<head>
    <style>
        p {
            color: red;
            font-size: 18px;
        }
    </style>
</head>
<body>
    <p>Paragraf ini berwarna merah.</p>
</body>
</html>
```

### c. External CSS (Menggunakan file terpisah dengan ekstensi `.css`)
1. Buat file `style.css`:
```css
p {
    color: green;
    font-size: 16px;
}
```
2. Hubungkan file CSS ke HTML:
```html
<head>
    <link rel="stylesheet" type="text/css" href="style.css">
</head>
```

## 3. Selektor CSS
### a. Selektor Elemen
Mengubah tampilan semua elemen tertentu.
```css
h1 {
    color: blue;
}
```

### b. Selektor ID
Menggunakan `#` untuk menargetkan satu elemen dengan ID tertentu.
```css
#judul {
    color: purple;
    font-size: 24px;
}
```
```html
<h1 id="judul">Judul Berwarna Ungu</h1>
```

### c. Selektor Class
Menggunakan `.` untuk menargetkan elemen dengan class tertentu.
```css
.teks-merah {
    color: red;
    font-weight: bold;
}
```
```html
<p class="teks-merah">Teks ini berwarna merah dan tebal.</p>
```

## 4. Properti Dasar CSS
### a. Warna
```css
p {
    color: blue;
    background-color: yellow;
}
```

### b. Font dan Teks
```css
p {
    font-size: 20px;
    font-family: Arial, sans-serif;
    text-align: center;
}
```

### c. Margin dan Padding
```css
div {
    margin: 20px;
    padding: 10px;
}
```

### d. Border (Garis Pinggir)
```css
div {
    border: 2px solid black;
}
```

## 5. Layout dengan CSS
### a. Display
```css
div {
    display: block;
}
span {
    display: inline;
}
```

### b. Flexbox (Membantu dalam tata letak)
```css
.container {
    display: flex;
    justify-content: center;
    align-items: center;
}
```

## 6. Kesimpulan
CSS sangat penting untuk mempercantik tampilan website. Dengan memahami dasar-dasar CSS ini, Anda bisa mulai mengatur gaya dan layout halaman web sesuai keinginan.

