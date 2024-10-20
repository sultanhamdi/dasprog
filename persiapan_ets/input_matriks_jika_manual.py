# input row dan collum
r, c = map(int,input().split())

#Proses mengisi nilai matriks
matriks = [list(map(int,input().split())) for _ in range (c)]

#Deklarasi variabel i dan j (sebagai penunjuk kolom dan baris) lalu variabel gold untuk menyimpan nilai gold
i, j = 0, 0
gold = matriks[i][j]
print(gold)