# Fallback heuristik sebelum model XGBoost dilatih — API tetap jalan.
def predict_omzet(jumlah_court:int, harga_sewa:float, jam_operasi_hari:float, hari_operasi:int, znt:float)->float:
    # ponytail: ceiling = heuristik kapasitas sederhana; upgrade ke XGBoost artifact saat tersedia
    kapasitas = jumlah_court * harga_sewa * jam_operasi_hari * hari_operasi * 4  # per bulan
    faktor_lokasi = 1.0 + min(znt/50_000_000, 0.5)  # premium boost capped
    return kapasitas * 0.45 * faktor_lokasi  # occupancy 45% default
