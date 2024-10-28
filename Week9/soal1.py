n = int(input("Masukkan sebuah angka: "))

def prima(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

    # Mengecek apakah n adalah bilangan prima
if prima(n):
    print("Bilangan tersebut prima")
else:
     print("Bilangan tersebut bukan prima")