import modul_sensor
 
# List kosong untuk menyimpan data berupa tuple (suhu, kelembaban)
log_kebun = []
 
 
def input_sensor():
    """Meminta input suhu dan kelembaban dengan validasi.
    Mengembalikan tuple (suhu, kelembaban)."""
 
    # Input suhu
    while True:
        try:
            suhu = float(input("Masukkan suhu udara (C) [0-100]: "))
            if 0 <= suhu <= 100:
                break
            else:
                print("Suhu harus di antara 0 sampai 100!")
        except ValueError:
            print("Input salah! Masukkan angka, bukan huruf.")
 
    # Input kelembaban
    while True:
        try:
            lembab = float(input("Masukkan kelembaban tanah (%) [0-100]: "))
            if 0 <= lembab <= 100:
                break
            else:
                print("Kelembaban harus di antara 0 sampai 100!")
        except ValueError:
            print("Input salah! Masukkan angka, bukan huruf.")
 
    return (suhu, lembab)
 
 
# ===== Program Utama =====
print("=== SISTEM MONITORING PRESISI IoT ===")
print("Lokasi:", modul_sensor.LOKASI[0])
print("Koordinat:", modul_sensor.LOKASI[1], ",", modul_sensor.LOKASI[2])
 
while True:
    print("\n----- MENU -----")
    print("[1] Rekam Data")
    print("[2] Analisis Tren (3 Terakhir)")
    print("[3] Keluar")
    pilihan = input("Pilih menu (1/2/3): ")
 
    if pilihan == "1":
        data_baru = input_sensor()
        log_kebun.append(data_baru)
        print("Data berhasil direkam:", data_baru)
 
    elif pilihan == "2":
        if len(log_kebun) == 0:
            print("Belum ada data. Silakan rekam data dulu (menu 1).")
        else:
            # Slicing: ambil maksimal 3 data terakhir
            tiga_terakhir = log_kebun[-3:]
 
            print("\nData", len(tiga_terakhir), "terakhir:")
            nomor = 1
            for data in tiga_terakhir:
                print(f"{nomor}. Suhu: {data[0]} C | Kelembaban: {data[1]} %")
                nomor += 1
 
            # Panggil fungsi dari modul
            rata_suhu, rata_lembab = modul_sensor.hitung_tren(tiga_terakhir)
            print(f"\nRata-rata suhu      : {rata_suhu:.2f} C")
            print(f"Rata-rata kelembaban: {rata_lembab:.2f} %")
 
            status = modul_sensor.evaluasi_irigasi(
                rata_suhu, rata_lembab, modul_sensor.AMBANG_KRITIS
            )
            print("Status:", status)
 
    elif pilihan == "3":
        print("Terima kasih. Program selesai.")
        break
 
    else:
        print("Pilihan tidak valid! Pilih 1, 2, atau 3.")