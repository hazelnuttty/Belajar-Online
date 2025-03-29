# Materi Dasar Python untuk Pemula

## 1. Pengertian Python
Python adalah bahasa pemrograman yang mudah dipahami dan digunakan untuk berbagai kebutuhan, seperti pengembangan web, data science, dan otomatisasi.

## 2. Menjalankan Python
Python bisa dijalankan di:
- Terminal atau Command Prompt dengan mengetik `python`
- File `.py` dengan perintah `python nama_file.py`

## 3. Variabel dan Tipe Data
### a. Deklarasi Variabel
```python
nama = "Rerey"
umur = 20
aktif = True
```

### b. Tipe Data
```python
teks = "Hello"  # String
angka = 10  # Integer
desimal = 3.14  # Float
boolean = True  # Boolean
array = [1, 2, 3]  # List
objek = {"nama": "Rerey", "umur": 20}  # Dictionary
```

## 4. Operator
```python
x = 10
y = 5
print(x + y)  # Penjumlahan (15)
print(x - y)  # Pengurangan (5)
print(x * y)  # Perkalian (50)
print(x / y)  # Pembagian (2.0)
print(x % y)  # Modulus (0)
```

## 5. Percabangan (If-Else)
```python
nilai = 80
if nilai >= 75:
    print("Lulus")
else:
    print("Tidak Lulus")
```

## 6. Perulangan (Looping)
### a. For Loop
```python
for i in range(1, 6):
    print(f"Angka {i}")
```

### b. While Loop
```python
i = 1
while i <= 5:
    print(f"Angka {i}")
    i += 1
```

## 7. Function (Fungsi)
```python
def sapa(nama):
    return f"Halo, {nama}!"

print(sapa("Rerey"))
```

## 8. List dan Dictionary
### a. List (Array)
```python
buah = ["apel", "mangga", "pisang"]
print(buah[0])  # Output: apel
```

### b. Dictionary (Object JSON)
```python
orang = {"nama": "Rerey", "umur": 20}
print(orang["nama"])  # Output: Rerey
```

## 9. Input dan Output
```python
nama = input("Masukkan nama: ")
print(f"Halo, {nama}!")
```

## 10. Kesimpulan
Python adalah bahasa pemrograman yang sederhana dan fleksibel. Dengan memahami dasar-dasar ini, Anda bisa mulai membuat program sendiri!

