# Input dari pengguna
M, N, T = map(int, input().split())
#keterangan M = banyak mobil di depan, N banyak mobil di belakang, T waktu dalam seconds.

# Total waktu dalam satu siklus lampu lalu lintas
cycle_time = 85  # 20  + 5  + 60

# Hitung sisa waktu setelah semua siklus penuh
remaining_time = T % cycle_time

# Waktu hijau yang tersedia
if remaining_time > 25:  # Melebihi waktu merah + kuning
    green_time = remaining_time - 25
else:
    green_time = 0

# Tambahkan waktu hijau dari siklus penuh
green_time += (T // cycle_time) * 60

# Hitung jumlah mobil yang bisa lewat
cars_passed = green_time // 5

# Tentukan apakah Anda bisa lewat
if cars_passed >= M + 1:  # Mobil ke-(M+1) adalah Anda
    # Hitung mobil yang tersisa di belakang Anda
    remaining_cars = max(0, (M + N) - cars_passed)
    print(f"YES! {remaining_cars}")
else:
    remaining_cars = (M + N) - cars_passed
    print(f"NO! {remaining_cars}")
