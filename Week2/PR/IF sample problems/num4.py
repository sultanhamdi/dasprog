#input
warna = input("Masukkan huruf pertama warna silinder (misalnya 'Y' untuk kuning): ").lower()

# Menentukan isi berdasarkan warna
if warna == 'o':
    isi = "amonia"
elif warna == 'b':
    isi = "karbon monoksida"
elif warna == 'y':
    isi = "hidrogen"
elif warna == 'g':
    isi = "oksigen"
else:
    isi = "Isi tidak diketahui"

#hasil
print(f"Isi dari silinder: {isi}")
