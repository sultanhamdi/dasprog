# Input jumlah barang dan uang
N, M = map(int, input().split())
    
# Input daftar harga barang
P = list(map(int, input().split()))
    
# Input daftar uang yang diberikan
C = list(map(int, input().split()))

# srotir nilai barang dan uang
P.sort()
C.sort()

# Jika semua nilai barang dan uang positif
if all(p > 0 for p in P) and all(c > 0 for c in C):
    if sum(P) > C[0]:
        hutang_maksimum = sum(P) - C[0]
        print(hutang_maksimum * -1)
    else:  # Misalnya dalam kasus ini, tidak ada hutang karena uangnya cukup atau lebih
        hutang_maksimum = 0
        print(hutang_maksimum * -1)
    
# Jika semua nilai barang dan uang negatif
elif all(p <= 0 for p in P) and all(c <= 0 for c in C):
    hutang_maksimum = sum(P) + sum(C)
    print(hutang_maksimum)

#jiika nilai barang ada yang positive dan negative dan nilai uang ada yang positive dan negative
else:
    # Menghitung total harga barang yang positif
    total_harga_positif = sum([p for p in P if p > 0])    
    # Menghitung total uang yang negatif
    total_uang_negatif = sum([c for c in C if c < 0])

    hutang_maksimum =  total_harga_positif - total_uang_negatif
    print(hutang_maksimum * -1)