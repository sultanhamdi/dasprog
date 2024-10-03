# input
N, K = map(int, input().split())
A = list(map(int, input().split()))

# Menghitung jumlah buah yang bisa dibeli
count = 0
for harga in A:
    if harga <= K:
        count += 1

# Output
print(count)
