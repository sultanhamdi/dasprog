def valid(x, y, M, N):
    return 0 <= x < M and 0 <= y < N

def Gerak(x, y, mall, dikunjungi, M, N, jalur, sisa_barang):
    if not valid(x, y, M, N):
        return False
    if mall[x][y] == '1':
        return False
    if dikunjungi[x][y]:
        return False
    
    dikunjungi[x][y] = True
    jalur.append((x, y))
    
    if mall[x][y] == '2':
        sisa_barang[0] -= 1
    
    if x == M-1 and y == N-1 and sisa_barang[0] == 0:
        return True
    
    if Gerak(x + 1, y, mall, dikunjungi, M, N, jalur, sisa_barang):
        return True
    if Gerak(x, y + 1, mall, dikunjungi, M, N, jalur, sisa_barang):
        return True
    if Gerak(x, y - 1, mall, dikunjungi, M, N, jalur, sisa_barang):
        return True
    if Gerak(x - 1, y, mall, dikunjungi, M, N, jalur, sisa_barang):
        return True
    
    dikunjungi[x][y] = False
    jalur.pop()
    if mall[x][y] == '2':
        sisa_barang[0] += 1
    return False

def hitung_barang(mall, M, N):
    jumlah = 0
    for i in range(M):
        for j in range(N):
            if mall[i][j] == '2':
                jumlah += 1
    return jumlah

N, M = map(int, input().split())
map = []
for _ in range(M):
    map.append(list(input().strip()))

dikunjungi = [[False] * N for _ in range(M)]
jalur = []

sisa_barang = [hitung_barang(map, M, N)]

ditemukan = Gerak(0, 0, map, dikunjungi, M, N, jalur, sisa_barang)

if ditemukan:
    hasil = [baris[:] for baris in map]
    for x, y in jalur:
        if hasil[x][y] != '1':
            hasil[x][y] = '*'
    
    for baris in hasil:
        print(''.join(baris))