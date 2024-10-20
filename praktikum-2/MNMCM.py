N = int(input())
bil = list(map(int, input().split()))

hasil = 1
for x in range(N):
    for y in range(x + 1, N):
        xor = bil[x] ^ bil[y]
        if xor == 0:
            print(0)
            exit()
        hasil *= xor

print(hasil)