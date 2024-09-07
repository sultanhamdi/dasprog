tinggi_bendungan = float(input("Masukkan tinggi bendungan (meter): "))
laju_aliran = float(input("Masukkan laju aliran air (meter kubik per detik): "))

#Konstanta
Gravitasi = 9.80  # konstanta gravitasi dalam m/s²
Efisensi = 0.90  # Efisensi 90%
massa_air_per_meter_kubik = 1000  # kg/m³

#menghitung work dalam detik
massa_per_detik = laju_aliran * massa_air_per_meter_kubik
Work = massa_per_detik * Gravitasi * tinggi_bendungan

#daya dalam watt
daya_watt = Work * Efisensi

#daya ke megawatt
daya_megawatt = daya_watt / 10**6

print(f"Daya yang dihasilkan: {daya_megawatt:.2f} MW")