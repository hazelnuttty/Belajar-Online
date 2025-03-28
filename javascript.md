# Materi Dasar JavaScript untuk Pemula

## 1. Pengertian JavaScript
JavaScript adalah bahasa pemrograman yang digunakan untuk menambahkan interaktivitas pada halaman web, seperti validasi form, animasi, dan manipulasi elemen HTML.

## 2. Cara Menggunakan JavaScript
Ada tiga cara menggunakan JavaScript:

### a. Inline JavaScript (Langsung dalam elemen HTML)
```html
<button onclick="alert('Halo, Dunia!')">Klik Saya</button>
```

### b. Internal JavaScript (Dalam tag `<script>` di file HTML)
```html
<!DOCTYPE html>
<html>
<head>
    <script>
        function sapa() {
            alert('Halo, Dunia!');
        }
    </script>
</head>
<body>
    <button onclick="sapa()">Klik Saya</button>
</body>
</html>
```

### c. External JavaScript (Menggunakan file `.js` terpisah)
1. Buat file `script.js`:
```js
function sapa() {
    alert('Halo, Dunia!');
}
```
2. Hubungkan file ke HTML:
```html
<head>
    <script src="script.js"></script>
</head>
```

## 3. Variabel dalam JavaScript
Tiga cara mendeklarasikan variabel:
```js
var nama = "Rerey"; // Bisa diubah
let umur = 20; // Bisa diubah
const kota = "Jakarta"; // Tidak bisa diubah
```

## 4. Tipe Data JavaScript
```js
let teks = "Hello"; // String
let angka = 10; // Number
let benar = true; // Boolean
let data = null; // Null
let tidakDiketahui; // Undefined
let daftar = [1, 2, 3]; // Array
let objek = { nama: "Rerey", umur: 20 }; // Object
```

## 5. Operator JavaScript
```js
let x = 10;
let y = 5;
console.log(x + y); // Penjumlahan (15)
console.log(x - y); // Pengurangan (5)
console.log(x * y); // Perkalian (50)
console.log(x / y); // Pembagian (2)
console.log(x % y); // Modulus (0)
```

## 6. Kondisi (If-Else dan Switch)
```js
let nilai = 80;
if (nilai >= 75) {
    console.log("Lulus");
} else {
    console.log("Tidak Lulus");
}
```

```js
let hari = "Senin";
switch (hari) {
    case "Senin":
        console.log("Hari kerja");
        break;
    case "Minggu":
        console.log("Hari libur");
        break;
    default:
        console.log("Hari tidak diketahui");
}
```

## 7. Perulangan (Looping)
### a. For Loop
```js
for (let i = 1; i <= 5; i++) {
    console.log("Angka " + i);
}
```

### b. While Loop
```js
let i = 1;
while (i <= 5) {
    console.log("Angka " + i);
    i++;
}
```

## 8. Function (Fungsi)
### a. Fungsi Biasa
```js
function sapa(nama) {
    return "Halo, " + nama;
}
console.log(sapa("Rerey"));
```

### b. Arrow Function
```js
const sapa = (nama) => "Halo, " + nama;
console.log(sapa("Rerey"));
```

## 9. Manipulasi DOM
### a. Mengubah Teks
```html
<p id="text">Teks awal</p>
<button onclick="ubahTeks()">Ubah</button>
<script>
function ubahTeks() {
    document.getElementById("text").innerHTML = "Teks berubah!";
}
</script>
```

### b. Mengubah Warna
```html
<p id="warna">Ubah warna teks ini</p>
<button onclick="ubahWarna()">Ubah Warna</button>
<script>
function ubahWarna() {
    document.getElementById("warna").style.color = "red";
}
</script>
```

## 10. Kesimpulan
JavaScript adalah bahasa pemrograman yang digunakan untuk membuat halaman web lebih interaktif. Dengan memahami dasar-dasar ini, Anda bisa mulai membangun fitur dinamis pada website Anda.

