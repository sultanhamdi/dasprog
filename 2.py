
# Input r dan c
r, c = map(int, input().split())

# Constraint
if 2 <= r <= 10 and 2 <= c <= 10:
    # Input elemen matriks
    arr = [list(map(int, input().split())) for _ in range(r)]
    
    # Inisialisasi variabel untuk menghitung korban
    kena = 0

    # Mengecek sudut
    sudut = [(0, 0), (0, c - 1), (r - 1, 0), (r - 1, c - 1)]
    for i, j in sudut:
        if arr[i][j] == 1:
            kena += 3

    # Mengecek sisi atas dan bawah (tanpa sudut)
    for j in range(1, c - 1):
        if arr[0][j] == 1:
            kena += 5
        if arr[r - 1][j] == 1:
            kena += 5

    # Mengecek sisi kiri dan kanan (tanpa sudut)
    for i in range(1, r - 1):
        if arr[i][0] == 1:
            kena += 5
        if arr[i][c - 1] == 1:
            kena += 5

    # Mengecek bagian tengah
    for i in range(1, r - 1):
        for j in range(1, c - 1):
            if arr[i][j] == 1:
                kena += 8

    for i in range(r):
        for j in range(j):
            if
            
    # Output hasil korban
    print(f"Korban = {kena}")