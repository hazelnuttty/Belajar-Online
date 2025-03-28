# Materi Dasar PHP untuk Pemula

## 1. Pengertian PHP
PHP (Hypertext Preprocessor) adalah bahasa pemrograman server-side yang digunakan untuk membuat halaman web dinamis dan berinteraksi dengan database.

## 2. Cara Menjalankan PHP
PHP dijalankan di server, jadi Anda memerlukan server lokal seperti XAMPP atau Laragon untuk menjalankan skrip PHP.

## 3. Struktur Dasar PHP
Kode PHP ditulis dalam tag `<?php ?>`.
```php
<?php
    echo "Halo, Dunia!";
?>
```

## 4. Variabel dan Tipe Data
### a. Variabel PHP
```php
<?php
    $nama = "Rerey";
    $umur = 20;
    echo "Nama saya $nama, umur saya $umur tahun.";
?>
```

### b. Tipe Data
```php
<?php
    $teks = "Halo"; // String
    $angka = 10; // Integer
    $desimal = 3.14; // Float
    $benar = true; // Boolean
    $array = ["apel", "mangga", "pisang"]; // Array
?>
```

## 5. Operator PHP
```php
<?php
    $x = 10;
    $y = 5;
    echo $x + $y; // 15
    echo $x - $y; // 5
    echo $x * $y; // 50
    echo $x / $y; // 2
    echo $x % $y; // 0
?>
```

## 6. Percabangan (If-Else dan Switch)
```php
<?php
    $nilai = 80;
    if ($nilai >= 75) {
        echo "Lulus";
    } else {
        echo "Tidak Lulus";
    }
?>
```

```php
<?php
    $hari = "Senin";
    switch ($hari) {
        case "Senin":
            echo "Hari kerja";
            break;
        case "Minggu":
            echo "Hari libur";
            break;
        default:
            echo "Hari tidak diketahui";
    }
?>
```

## 7. Perulangan (Looping)
### a. For Loop
```php
<?php
    for ($i = 1; $i <= 5; $i++) {
        echo "Angka $i <br>";
    }
?>
```

### b. While Loop
```php
<?php
    $i = 1;
    while ($i <= 5) {
        echo "Angka $i <br>";
        $i++;
    }
?>
```

## 8. Function (Fungsi)
```php
<?php
    function sapa($nama) {
        return "Halo, $nama";
    }
    echo sapa("Rerey");
?>
```

## 9. Form Handling (Mengambil Data dari Form)
```html
<form action="proses.php" method="post">
    Nama: <input type="text" name="nama">
    <input type="submit" value="Kirim">
</form>
```

```php
// proses.php
<?php
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        $nama = $_POST["nama"];
        echo "Halo, $nama!";
    }
?>
```

## 10. Koneksi ke Database (MySQLi)
```php
<?php
    $conn = new mysqli("localhost", "root", "", "database");
    if ($conn->connect_error) {
        die("Koneksi gagal: " . $conn->connect_error);
    }
    echo "Koneksi berhasil";
?>
```

## 11. Kesimpulan
PHP digunakan untuk membuat website dinamis dan berinteraksi dengan database. Dengan memahami dasar-dasar ini, Anda bisa mulai membangun aplikasi web sederhana.

