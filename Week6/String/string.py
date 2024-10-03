string_0 = "Sultan Hamdi Jailani Daulay"
string_1 = "5054241013"
string_2 = "Medan"

print("Nama saya adalah " + string_0)
print("NRP  " + string_1)
print("Asal daerah " + string_1)
print("Inisial saya " + string_0[0] + string_0[7] + string_0[13] + string_0[-6])
print("Nama belakang " + string_0[-6:])
print("Nama panggilan " + string_0[0:6])
print("NRP dibalik " + string_1[::-1])

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