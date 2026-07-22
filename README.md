<p align="center">
    <img src="https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExaXY0djYzeW5hZWk1NmpsdzMzNnhsa2VuN3oxZTgyNzA5aGl3NGw3MyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/sQtQfluTIBeuTOWJRq/giphy.gif" width="50%" height="50%" alt="Re7Pntx"/>
    <br>
    <a href="https://github.com/Rlxfly"><img title="Created by" src="https://img.shields.io/badge/Created%20by-Re7Pntx-cyan?style=for-the-badge&logo=github"></a>
</p>

# Statistik Luas Area Kopi Robusta di Kabupaten Lima Puluh Kota
---------------
```
Nama: Mikael Christian Farrel
NIM: 25.11.6408
Kelas: IF03
```

## Apa fungsi dari program ini?
Program ini berfungsi untuk membuat diagram batang dari data yang diberikan dan menghitung rata-rata dari data tersebut

# How to use?

```python
python main.py
```
### Or...
```python
python3 main.py
```
# Beberapa fungsi yang saya pakai di dalam file `utils.py`
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `muat_data(filepath)` | `path` | Membaca file CSV |
| `bersihkan_data(df)` | `file` | Membersihkan data yang tidak konsisten |
| `hitung_statistik(df)` | `file` | Melakukan perhitungan statistik & mengembalikan teks berupa string |
| `simpan_ringkasan_txt(filepath, teks)` | `path, text` | Menulis hasil ringkasan ke file teks |
| `buat_grafik(df, filepath_output)` | `file, path` | Membuat 2 jenis grafik menggunakan Matplotlib |

# Contoh cara memakai fungsi dari file `utils.py`

```python
  import utils

def main():
    print("┏━[ Memulai Program Analisis Data ]━━━━━━━━")
    
    # Tentukan path/lokasi
    path_dataset = 'dataset/data_mentah.csv'
    path_output_txt = 'hasil_analisis.txt'
    path_output_gambar = 'grafik_output.png'
    
    # Proses Muat Data
    print("┃    [⌛] Membaca dataset...     ")
    df = utils.muat_data(path_dataset)
```

# Preview output
------------------
- [x] Output dari terminal <details><summary>Screenshot</summary><img src="https://i.ibb.co/7xMnpxYd/image.png"></details>
- [x] Data .csv mentah <details><summary>Screenshot</summary><img src="https://i.ibb.co/nsJqBvCq/image.png"></details>
- [x] Data .csv yang sudah di filter dan diurutkan <details><summary>Screenshot</summary><img src="https://i.ibb.co/fd1JH2SG/image.png"></details>
- [x] Visualisasi diagramnya <details><summary>Screenshot</summary><img src="https://i.ibb.co/fYPMz8hw/image.png"></details>
------------------
## Data di atas saya ambil dari [web ini](https://data.go.id/dataset/dataset/luas-area-kopi-robusta-di-kabupaten-lima-puluh-kota)
------------------

## Authors

[![Rlxfly](https://github.com/Rlxfly.png?size=100)](https://github.com/Rlxfly)


## Library that i use


![lol](https://img.shields.io/badge/Using-Pandas-blue.svg
)
![lol](https://img.shields.io/badge/And-Matplotlib-yellow
)
