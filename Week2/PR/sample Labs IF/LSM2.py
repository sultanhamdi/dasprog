# Input data
N, C = map(int, input().split())
# N adalah banyaknya bola
# C menentukan urutan main, C = 1 (Lala) C = 2 (Lili)

# Cek siapa yang akan menang
if N % 8 == 0:
    winner = "Lili" if C == 1 else "Lala"
else:
    winner = "Lala" if C == 1 else "Lili"

# Output pemenang
print(winner)
