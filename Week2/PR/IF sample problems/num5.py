#input
data_usage = float(input("Masukkan jumlah penggunaan data dalam Gbs: "))

# Menghitung biaya berdasarkan penggunaan data
if 0.0 < data_usage <= 1.0:
    charges = 250
elif 1.0 < data_usage <= 2.0:
    charges = 500
elif 2.0 < data_usage <= 5.0:
    charges = 1000
elif 5.0 < data_usage <= 10.0:
    charges = 1500
elif data_usage > 10.0:
    charges = 2000
else:
    charges = None

if charges is not None:
    print(f"\nBiaya yang harus dibayar: ${charges}")
else:
    print("\nData yang dimasukkan tidak valid. Silakan masukkan nilai yang positif.")
