import pandas as pd
import matplotlib.pyplot as plt

def muat_data(filepath):
    """
    Membuka file CSV dan mengembalikan DataFrame.
    """
    df = pd.read_csv(filepath, sep=';')
    return df

def bersihkan_data(df):
    """
    Membersihkan data yang tidak diperlukan dan mengisi nilai kosong.
    """
    # Menghapus spasi kosong di awal/akhir teks pada kolom 'uraian' (Luas Lahan (Ha))
    if 'uraian' in df.columns:
        df['uraian'] = df['uraian'].str.strip()
    
    # Mengisi nilai kosong pada kolom 'keterangan' dengan tanda '-'
    if 'keterangan' in df.columns:
        df['keterangan'] = df['keterangan'].fillna('-')
        
    # Mengisi nilai kosong pada kolom angka dengan 0
    df = df.fillna(0)
    
    return df

def hitung_statistik(df):
    """
    Melakukan perhitungan statistik
    Membentuk ringkasan statistik dalam bentuk teks yang dapat disimpan ke file 'hasil_analisis.txt'
    """
    teks = "----- RINGKASAN STATISTIK LUAS LAHAN -----\n\n"
    
    # Menghitung Total Luas Lahan per Tahun
    total_2022 = df['2022'].sum()
    total_2023 = df['2023'].sum()
    total_2024 = df['2024'].sum()
    
    teks += f"Total Luas Lahan Tahun 2022: {total_2022} Ha\n"
    teks += f"Total Luas Lahan Tahun 2023: {total_2023} Ha\n"
    teks += f"Total Luas Lahan Tahun 2024: {total_2024} Ha\n\n"
    
    # Mencari Daerah dengan Lahan Terbesar di Tahun 2024
    idx_max = df['2024'].idxmax()
    daerah_max = df.loc[idx_max, 'uraian']
    nilai_max = df.loc[idx_max, '2024']
    
    teks += f"Daerah dengan Lahan Terluas (2024): {daerah_max} ({nilai_max} Ha)\n"
    
    # Menghitung Rata-rata Luas Lahan pada Tahun 2024
    rata_rata_2024 = df['2024'].mean()
    teks += f"Rata-rata Luas Lahan per Daerah (2024): {rata_rata_2024:.2f} Ha\n----------------------------------------------\n"
    
    return teks

def simpan_ringkasan_txt(filepath, teks):
    """
    Menulis hasil ringkasan statistik ke file .txt
    """
    with open(filepath, 'w') as file:
        file.write(teks)
    print(f"┃    [❗] File ringkasan statistik berhasil disimpan di: {filepath}")

def buat_grafik(df, filepath_output):
    """
    Membuat 2 jenis visualisasi menggunakan Matplotlib
    """
    # Membuat canvas
    fig, axes = plt.subplots(1, 4, figsize=(25, 5))
    
    # --- Grafik 1: Bar Plot (Luas Lahan Tiap Daerah Tahun 2022) ---
    axes[0].barh(df['uraian'], df['2022'], color='skyblue', edgecolor='black')
    axes[0].set_title('Luas Lahan Tiap Daerah (Tahun 2022)')
    axes[0].set_xlabel('Luas Lahan (Ha)')
    axes[0].set_ylabel('Nama Daerah')
    axes[0].tick_params(axis='x', rotation=0) 

     # --- Grafik 1: Bar Plot (Luas Lahan Tiap Daerah Tahun 2023) ---
    axes[1].barh(df['uraian'], df['2023'], color='skyblue', edgecolor='black')
    axes[1].set_title('Luas Lahan Tiap Daerah (Tahun 2023)')
    axes[1].set_xlabel('Luas Lahan (Ha)')
    axes[1].set_ylabel('Nama Daerah')
    axes[1].tick_params(axis='x', rotation=0)

     # --- Grafik 1: Bar Plot (Luas Lahan Tiap Daerah Tahun 2024) ---
    axes[2].barh(df['uraian'], df['2024'], color='skyblue', edgecolor='black')
    axes[2].set_title('Luas Lahan Tiap Daerah (Tahun 2024)')    
    axes[2].set_xlabel('Luas Lahan (Ha)')    
    axes[2].set_ylabel('Nama Daerah')
    axes[2].tick_params(axis='x', rotation=0)              
    
    
    # --- Grafik 2: Line Plot (Tren Total Keseluruhan 2022-2024) ---
    tahun = ['2022', '2023', '2024']
    total_luas = [df['2022'].sum(), df['2023'].sum(), df['2024'].sum()]
    
    axes[3].plot(tahun, total_luas, marker='o', color='green', linestyle='-', linewidth=2)
    axes[3].set_title('Tren Total Luas Lahan (2022 - 2024)')
    axes[3].set_xlabel('Tahun')
    axes[3].set_ylabel('Total Luas (Ha)')
    axes[3].grid(True, linestyle='--', alpha=0.6)
    
    # Merapikan jarak
    plt.tight_layout()
    
    # Menyimpan grafik sebagai gambar
    plt.savefig(filepath_output)
    plt.close() # Mengakhiri sesi plotting
    print(f"┃    [❗] Grafik visualisasi berhasil disimpan di: {filepath_output}")