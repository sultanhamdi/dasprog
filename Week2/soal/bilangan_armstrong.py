#input user
angka = int(input("masukkan angka =>"))
#untuk ratusan
if (100 <= angka < 1000):
    A = int(angka%10)
    B = int((angka//10)%10)
    C = int(angka//100)
    if(angka == (A**3)+(B**3)+(C**3)):
        print(angka,"adalah bilangan armstrong")
    else:
        print(angka,"bukan bilangan armstrong")
#untuk puluhan
if (10 <= angka < 100):
    A = int(angka%10)
    B = int((angka//10)%10)
    if(angka == (A**2)+(B**2)):
        print(angka,"adalah bilangan armstrong")
    else:
        print(angka,"bukan bilangan armstrong")
#untuk satuan
if (1 <= angka < 10):
    A = int(angka%10)
    if(angka == (A**1)):
        print(angka,"adalah bilangan armstrong")
    else:
        print(angka,"bukan bilangan armstrong")