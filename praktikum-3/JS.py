def cek_valid(N, M, max_rows, max_colls):
    if N < 0 or M < 0:
        return False
    if N >= max_rows or M >= max_colls:
        return False
    return True

def jalan(N, M, grid, visited, max_rows, max_colls, path, sisa):
    # Cek apakah bisa jalan
    if not cek_valid(N, M, max_rows, max_colls):
        return False
    if grid[N][M] == '1':
        return False
    if visited[N][M]:
        return False

    visited[N][M] = True
    path.append((N, M))

    if grid[N][M] == '2':
        sisa[0] = sisa[0] - 1

    if N == max_rows-1 and M == max_colls-1 and sisa[0] == 0:
        return True

    if jalan(N+1, M, grid, visited, max_rows, max_colls, path, sisa):
        return True
    if jalan(N, M+1, grid, visited, max_rows, max_colls, path, sisa):
        return True
    if jalan(N, M-1, grid, visited, max_rows, max_colls, path, sisa):
        return True
    if jalan(N-1, M, grid, visited, max_rows, max_colls, path, sisa):
        return True
    
    # Mundur kalau tidak path_found jalan
    visited[N][M] = False
    path.pop()
    if grid[N][M] == '2':
        sisa[0] = sisa[0] + 1
    return False

def hitung_barang(grid, max_rows, max_colls):
    total = 0
    for i in range(max_rows):
        for j in range(max_colls):
            if grid[i][j] == '2':
                total = total + 1
    return total

M, N = input().split()
M = int(M)
N = int(N)

grid = []
for i in range(N):
    grid.append(list(input()))

visited = []
for i in range(N):
    baris_baru = []
    for j in range(M):
        baris_baru.append(False)
    visited.append(baris_baru)

path = []
sisa = [hitung_barang(grid, N, M)]

path_found = jalan(0, 0, grid, visited, N, M, path, sisa)

if path_found:
    hasil = []
    for i in range(N):
        baris_hasil = []
        for j in range(M):
            baris_hasil.append(grid[i][j])
        hasil.append(baris_hasil)
    
    for b, k in path:
        if hasil[b][k] != '1':
            hasil[b][k] = '*'
    
    for baris_hasil in hasil:
        print(''.join(baris_hasil))