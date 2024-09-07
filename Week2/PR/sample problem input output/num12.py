kecepatan_kmph = float(input("Masukkan kecepatan lepas landas jet (km/jam): "))
jarak_m = float(input("Masukkan jarak percepatan ketapel (meter): "))

# Konversi kecepatan dari km/jam ke m/s
kecepatan_mps = kecepatan_kmph * (1000 / 3600)

# Menghitung percepatan menggunakan rumus a = v^2 / (2s)
percepatan = (kecepatan_mps ** 2) / (2 * jarak_m)

# Menghitung waktu yang diperlukan untuk mencapai kecepatan lepas landas menggunakan rumus t = v / a
waktu = kecepatan_mps / percepatan

# Menampilkan hasil percepatan dan waktu
print(f"Percepatan: {percepatan:.2f} m/s²")
print(f"Waktu untuk mencapai kecepatan lepas landas: {waktu:.2f} detik")