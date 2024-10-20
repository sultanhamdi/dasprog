N, r, c = map(int, input().split())

# Membuat array matriks kosong
seat = [[0] * c for i in range(r)]

# Memasukkan data nilai ke dalam array
data = []
for i in range(N):
    x, a, b = map(int, input().split())
    seat[a-1][b-1] = x  # Memasukkan data ke tempat duduk
    data.append((x, a-1, b-1))  # Menyimpan data