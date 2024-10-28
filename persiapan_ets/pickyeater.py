n = int(input())  # Jumlah siswa
pilihan_buah = list(map(int, input().split()))  # Daftar pilihan buah tiap siswa
# Inisialisasi daftar untuk menghitung frekuensi tiap ID buah (1-10)
jumlah_buah = [0] * 11  # Index 0 tidak dipakai, ID buah dimulai dari 1 hingga 10

# Menghitung frekuensi masing-masing ID buah
for buah in pilihan_buah:
    jumlah_buah[buah] += 1

# Mencari ID buah dengan frekuensi terbanyak
max_jumlah = 0
buah_terbanyak = -1

for id_buah in range(1, 11):
    if jumlah_buah[id_buah] > max_jumlah:
        max_jumlah = jumlah_buah[id_buah]
        buah_terbanyak = id_buah

# Memeriksa apakah buah ini memiliki mayoritas yang ketat (lebih dari setengah jumlah siswa)
if max_jumlah > n // 2:
    perubahan_dibutuhkan = n - max_jumlah
    print(buah_terbanyak)
    print(perubahan_dibutuhkan)
else:
    print(-1)
