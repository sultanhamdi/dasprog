def count_odd_numbers(list_angka):
    ganjil = 0  
    
    for num in list_angka:
        if num % 2 != 0:  
            ganjil += 1  

    return ganjil

# Input list angka dari pengguna
list_angka = list(map(int, input("Masukkan deret angka (dipisahkan spasi): ").split()))
hasil = count_odd_numbers(list_angka)
print("Total angka ganjil: ", hasil)

