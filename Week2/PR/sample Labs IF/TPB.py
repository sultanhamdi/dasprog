# Input dari pengguna
n = int(input("Masukkan sebuah angka: "))

    # Fungsi untuk memeriksa apakah n adalah bilangan prima
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

    # Mengecek apakah n adalah bilangan prima
if is_prime(n):
    print("IT IS A PRIME")
else:
     print("IT IS NOT A PRIME")