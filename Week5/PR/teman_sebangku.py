# Input
N, r, c = map(int, input().split())

# Membuat array tempat duduk
seat = [[0] * c for i in range(r)]

# Memasukkan data siswa ke dalam array
siswa = []
for i in range(N):
    x, a, b = map(int, input().split())
    seat[a-1][b-1] = x  # Memasukkan siswa ke tempat duduk
    siswa.append((x, a-1, b-1))  # Menyimpan data siswa

# Proses untuk mencari siswa yang duduk di sebelah
for x, a, b in siswa:
    if b > 0 and seat[a][b-1] != 0:  # Cek sebelah kiri
        print(seat[a][b-1])
    elif b < c-1 and seat[a][b+1] != 0:  # Cek sebelah kanan
        print(seat[a][b+1])
    else:
        print(0)