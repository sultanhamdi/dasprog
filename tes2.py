cache_ubin = {}

def cara_ubin(n):
    if n in cache_ubin:
        return cache_ubin[n]
    
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        cache_ubin[n] = cara_ubin(n - 1) + cara_ubin(n - 2)
        return cache_ubin[n]
n = int(input())
print("Jumlah cara untuk menyusun lantai ukuran 2 x 5 adalah:", cara_ubin(n))
print("Cache hasil perhitungan:", cache_ubin)
