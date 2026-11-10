LOKASI = ("Kampung Anggur Plumbungan", -7.828, 110.378)
AMBANG_KRITIS = (35.0, 40.0)  # (Suhu Max, Kelembaban Min)
 
 
def hitung_tren(data_slice):
    """Menghitung rata-rata suhu dan rata-rata kelembaban
    dari list berisi tuple (suhu, kelembaban)."""
    total_suhu = 0
    total_lembab = 0
 
    for data in data_slice:
        total_suhu += data[0]
        total_lembab += data[1]
 
    jumlah = len(data_slice)
    rata_suhu = total_suhu / jumlah
    rata_lembab = total_lembab / jumlah
 
    return rata_suhu, rata_lembab
 
 
def evaluasi_irigasi(rata_suhu, rata_lembab, tuple_kritis):
    """Menentukan status pompa irigasi berdasarkan ambang kritis."""
    suhu_max = tuple_kritis[0]
    lembab_min = tuple_kritis[1]
 
    if rata_suhu > suhu_max or rata_lembab < lembab_min:
        return "KRITIS: Nyalakan Pompa Irigasi!"
    else:
        return "NORMAL: Pompa Mati."
