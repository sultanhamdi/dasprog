panjang_rumah = float(input("panjang rumah anda (dalam satuan kaki)"))
lebar_rumah = float(input("lebar rumah anda (dalam satuan kaki)"))

panjang_lapangan = float(input("panjang lapangan anda"))
lebar_lapangan = float(input("lebar lapangan anda"))

luas_rumah = panjang_rumah * lebar_rumah 
luas_lapangan = panjang_lapangan * lebar_lapangan
rumput = luas_lapangan - luas_rumah
waktu = rumput/2
print(waktu, "detik")