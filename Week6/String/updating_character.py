# mengupdate sebuah karakter di string

# Cara pertama
string1 = "Saya mahasiswa RKA"
list1 = list(string1)
list1[5:] = 'bukan mahasiswa RPL'
string2 = ''.join(list1)
print(string2)

# Cara kedua
string1 = "Saya mahasiswa RKA"
print(string1)

string2 = string1[0:4] + " bukan " + string1[5:14] + " RPL "
print(string2)