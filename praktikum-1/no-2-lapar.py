# Input ukuran ruangan dungeon
X, Y = map(int, input().split())

# Input posisi Senshi
x, y = map(int, input().split())

# Input jumlah monster
M = int(input())

# Inisialisasi posisi monster secara manual hingga maksimal 8 monster
monster1 = monster2 = monster3 = monster4 = monster5 = monster6 = monster7 = monster8 = (-1, -1)

if M > 0:
    mx1, my1 = map(int, input().split())
    monster1 = (mx1, my1)
if M > 1:
    mx2, my2 = map(int, input().split())
    monster2 = (mx2, my2)
if M > 2:
    mx3, my3 = map(int, input().split())
    monster3 = (mx3, my3)
if M > 3:
    mx4, my4 = map(int, input().split())
    monster4 = (mx4, my4)
if M > 4:
    mx5, my5 = map(int, input().split())
    monster5 = (mx5, my5)
if M > 5:
    mx6, my6 = map(int, input().split())
    monster6 = (mx6, my6)
if M > 6:
    mx7, my7 = map(int, input().split())
    monster7 = (mx7, my7)
if M > 7:
    mx8, my8 = map(int, input().split())
    monster8 = (mx8, my8)

# Cek apakah ada ubin kosong di sekeliling Senshi
ubin_kosong = False

# Cek atas
if x > 0:
    if not ((x-1, y) == monster1 or (x-1, y) == monster2 or (x-1, y) == monster3 or
            (x-1, y) == monster4 or (x-1, y) == monster5 or (x-1, y) == monster6 or
            (x-1, y) == monster7 or (x-1, y) == monster8):
        ubin_kosong = True

# Cek bawah
if not ubin_kosong and x < X-1:
    if not ((x+1, y) == monster1 or (x+1, y) == monster2 or (x+1, y) == monster3 or
            (x+1, y) == monster4 or (x+1, y) == monster5 or (x+1, y) == monster6 or
            (x+1, y) == monster7 or (x+1, y) == monster8):
        ubin_kosong = True

# Cek kiri
if not ubin_kosong and y > 0:
    if not ((x, y-1) == monster1 or (x, y-1) == monster2 or (x, y-1) == monster3 or
            (x, y-1) == monster4 or (x, y-1) == monster5 or (x, y-1) == monster6 or
            (x, y-1) == monster7 or (x, y-1) == monster8):
        ubin_kosong = True

# Cek kanan
if not ubin_kosong and y < Y-1:
    if not ((x, y+1) == monster1 or (x, y+1) == monster2 or (x, y+1) == monster3 or
            (x, y+1) == monster4 or (x, y+1) == monster5 or (x, y+1) == monster6 or
            (x, y+1) == monster7 or (x, y+1) == monster8):
        ubin_kosong = True

# Output hasil
if ubin_kosong:
    print("Senshi makan hari ini!")
else:
    print("Senshi makannya besok aja deh.")
