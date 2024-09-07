#input dari pengguna
total_pembelian = float(input("Masukkan total pembelian: $"))
student = input("Apakah pembeli seorang siswa? (yes/no): ").lower()

besar_diskon_siswa = 0.20
pajak_penjualan = 0.05

# Menghitung diskon jika pembeli adalah siswa
if student == "yes":
    diskon_siswa = total_pembelian * besar_diskon_siswa
    total_diskon = total_pembelian - diskon_siswa
else:
    diskon_siswa = 0
    total_diskon = total_pembelian

# Menghitung pajak penjualan berdasarkan total setelah diskon
pajak = total_diskon * pajak_penjualan

# Menghitung total akhir setelah pajak
total_akhir = total_diskon + pajak

# Menampilkan hasil
print(f"\nTotal pembelian: ${total_pembelian:.2f}")
if student == "yes":
    print(f"Diskon siswa (20%): ${diskon_siswa:.2f}")
    print(f"Total setelah diskon: ${total_diskon:.2f}")
print(f"Pajak penjualan (5%): ${pajak:.2f}")
print(f"Total: ${total_akhir:.2f}")
