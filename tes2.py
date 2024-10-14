# Membaca input
T = int(input())  # Jumlah N makanan & minuman
N = list(map(int, input().split()))  # Daftar N makanan & minuman

# Langkah 1: Mencari N maksimum untuk menentukan ukuran array frekuensi
max_harga = max(N)  # Harga tertinggi untuk membuat array frekuensi yang cukup besar

# Langkah 2: Membuat array untuk menghitung frekuensi tiap N
frekuensi = [0] * (max_harga + 1)  # Array frekuensi, ukuran sesuai dengan N maksimum

# Langkah 3: Menghitung frekuensi setiap N
for i in N:
    frekuensi[i] += 1  # Tambahkan frekuensi setiap kali N muncul

# Langkah 4: Mencari modus (N dengan frekuensi tertinggi)
max_frekuensi = 0
modus = 0

for i in range(max_harga + 1):
    if frekuensi[i] > max_frekuensi:
        max_frekuensi = frekuensi[i]
        modus = i
    elif frekuensi[i] == max_frekuensi and i > modus:
        modus = i

# Langkah 5: Mengecek apakah modus adalah bilangan prima
prima = True
if modus < 2:
    prima = False  # Bilangan kurang dari 2 bukan prima
else:
    for i in range(2, int(modus ** 0.5) + 1):
        if modus % i == 0:
            prima = False
            break

# Langkah 6: Output sesuai dengan hasil
print(f"Modus: {modus}")
if prima:
    print("Wah, modenya prima nihh.")
else:
    print("Yah, modenya gak prima.")
