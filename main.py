import utils

def main():
    print("┏━[ Memulai Program Analisis Data ]━━━━━━━━")
    
    path_dataset = 'dataset/data_mentah.csv'
    path_output_txt = 'hasil_analisis.txt'
    path_output_gambar = 'grafik_output.png'
    
    print("┃    [⌛] Membaca dataset...     ")
    df = utils.muat_data(path_dataset)
    
    print("┃    [⌛] Membersihkan data...     ")
    df_bersih = utils.bersihkan_data(df)
    
    print("┃    [⌛] Menghitung statistik dan menyimpan file .txt...     ")
    teks_statistik = utils.hitung_statistik(df_bersih)
    utils.simpan_ringkasan_txt(path_output_txt, teks_statistik)
    
    print("┃    [⌛] Membuat grafik dan menyimpan file .png...     ")
    utils.buat_grafik(df_bersih, path_output_gambar)
    
    print("┃    Program Selesai Eksekusi dengan Sukses!")
    print("┗━[ Silakan cek file 'hasil_analisis.txt' dan 'grafik_output.png' di folder Anda ]━━━━━━━")

if __name__ == "__main__":
    main()