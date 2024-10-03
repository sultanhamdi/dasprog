# input r,c, dan N
r, c, N = map(int,input().split())

#Proses mengisi nilai hutan hutan
hutan = [list(map(int,input().split())) for _ in range (c)]

#Input pergerakan dengan karakter tanpa spasi sebanyak N digit
arah_gerak = input() 

#Deklarasi variabel i dan j (sebagai penunjuk kolom dan baris) lalu variabel gold untuk menyimpan nilai gold
i, j = 0, 0
gold = hutan[i][j]

#Melakukan looping untuk mengecek setiap pergerakan dan menghitung perubahan jumlah gold

for kak_gem in arah_gerak:
    if kak_gem == 'R':
        j += 1
        if j > (c - 1):
            arah_gerak = False 
            break
        gold += hutan[i][j]
        gold += 3
    elif kak_gem == 'L':
        j -= 1
        if j < 1:
            arah_gerak = False
            break
        gold += hutan[i][j]
        gold -= 2
    elif kak_gem == 'U':
        i -= 1
        if i < 1:
            arah_gerak = False
            break
        gold += hutan[i][j]
        gold += 3
    elif kak_gem == 'D':
        i += 1
        if i > r - 1:
            arah_gerak = False
            break
        gold += hutan[i][j]
        gold -= 2
    else:
        print("Masukkan R, L, U, dan D bukan yang lain")



#Proses untuk menampilkan output :
if arah_gerak == False:
    print(gold)
    print("gerakanmu salah bung!")
else:
    print(gold)