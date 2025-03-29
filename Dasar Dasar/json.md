# Materi Dasar JSON untuk Pemula

## 1. Pengertian JSON
JSON (JavaScript Object Notation) adalah format data yang ringan dan mudah dibaca oleh manusia serta mesin. JSON digunakan untuk bertukar data antar aplikasi, terutama dalam komunikasi API.

## 2. Struktur JSON
JSON menggunakan pasangan key-value dengan format berikut:
```json
{
    "nama": "Rerey",
    "umur": 20,
    "kota": "Jakarta"
}
```

## 3. Tipe Data dalam JSON
### a. String
```json
{
    "nama": "Rerey"
}
```

### b. Number
```json
{
    "umur": 20,
    "tinggi": 170.5
}
```

### c. Boolean
```json
{
    "aktif": true
}
```

### d. Array
```json
{
    "hobi": ["membaca", "coding", "gaming"]
}
```

### e. Object (Nested JSON)
```json
{
    "nama": "Rerey",
    "alamat": {
        "kota": "Jakarta",
        "negara": "Indonesia"
    }
}
```

## 4. Cara Menggunakan JSON di JavaScript
### a. Parsing JSON (Mengubah JSON ke JavaScript Object)
```js
let data = '{ "nama": "Rerey", "umur": 20 }';
let obj = JSON.parse(data);
console.log(obj.nama); // Output: Rerey
```

### b. Stringify JSON (Mengubah JavaScript Object ke JSON)
```js
let obj = { nama: "Rerey", umur: 20 };
let jsonStr = JSON.stringify(obj);
console.log(jsonStr);
```

## 5. JSON dalam PHP
### a. Decode JSON ke Array PHP
```php
<?php
$json = '{"nama": "Rerey", "umur": 20}';
$data = json_decode($json, true);
echo $data["nama"]; // Output: Rerey
?>
```

### b. Encode Array PHP ke JSON
```php
<?php
$data = ["nama" => "Rerey", "umur" => 20];
echo json_encode($data);
?>
```

## 6. Kesimpulan
JSON adalah format pertukaran data yang sering digunakan dalam API dan komunikasi antar aplikasi. Dengan memahami JSON, Anda bisa mengolah data dengan lebih mudah dan efisien.

