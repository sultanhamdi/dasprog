# Input dari pengguna
a = list(map(int, input().split()))
b = int(input())
c = int(input())
d, e, f = map(int, input().split())

# Hitung jumlah rotasi efektif
effective_rotations = c % 7

# Lakukan rotasi sebanyak effective_rotations kali
for _ in range(effective_rotations):
    a = a[-b:] + a[:-b]

# Output nilai yang sesuai dengan indeks yang diminta
print(a[d], a[e], a[f])