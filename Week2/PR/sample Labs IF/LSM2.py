
#input
N, C = map(int, input("Banyak bola dan siapa yang mulai (angka 1 atau 2)=>").split())
#N adalah jumlah bola
#C adalah penentu diapa yang memulai, 1 untuk Lala, 2 untuk Lili

# Jika N mod 7 == 0, maka posisi kalah bagi pemain yang memulai
if N % 7 == 0:
    winner = "Lili" if C == 1 else "Lala"
else:
    winner = "Lala" if C == 1 else "Lili"

print(winner)