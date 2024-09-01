#input m dan n
m = int(input("Masukkan nilai m (bilangan bulat positif): "))
n = int(input("Masukkan nilai n (bilangan bulat positif): "))

if (m>n):
#rumus
    side1 = m**2 - n**2
    side2 = 2 * m * n
    hypotenuse = m**2 + n**2

    print("Side1 =", side1)
    print("Side2 =", side2)
    print("Hipotenusa=", hypotenuse)
else :
    print("m harus lebih besar dari n")