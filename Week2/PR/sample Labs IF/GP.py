# Input: string berisi jarak lompatan maksimum dan jarak antara pilar-pilar
inputs = input().split()  # Memisahkan input menjadi daftar angka
n = int(inputs[0])  # Angka pertama adalah jarak lompatan maksimum B
distances = list(map(int, inputs[1:]))  # Angka selanjutnya adalah jarak antar pilar

# Asumsi awal bahwa B bisa melompat ke semua pilar
can_jump = "YES HE CAN"

# Memeriksa apakah setiap jarak antara pilar-pilar dapat dijangkau oleh B
for distance in distances:
    if distance > n:  # Jika ada jarak yang lebih besar dari jarak maksimum
        can_jump = "NO HE CAN'T"
        break  # Keluar dari loop jika ada jarak yang tidak bisa dijangkau

# Output hasilnya
print(can_jump)