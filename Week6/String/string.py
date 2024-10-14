string_0 = "Sultan Hamdi Jailani Daulay"
string_1 = "5054241013"
string_2 = "Medan"

# Print string
print("Nama saya adalah " + string_0)
print("NRP  " + string_1)
print("Asal daerah " + string_1)

# Access Character in String
print("Inisial saya " + string_0[0] + string_0[7] + string_0[13] + string_0[-6])

# String Slicing
print("Nama belakang " + string_0[-6:])
print("Nama panggilan " + string_0[0:6])

# Reversed String
print("NRP dibalik " + string_1[::-1])

# mengupdate sebuah karakter di string
# Cara pertama
string_3 = "Saya mahasiswa RKA"
list3 = list(string_3)
list3[5:] = 'bukan mahasiswa RPL'
string_4 = ''.join(list3)
print(string_4)

# Cara kedua
string_3 = "Saya mahasiswa RKA"
print(string_3)
string_4 = string_3[0:4] + " bukan " + string_3[5:14] + " RPL "
print(string_4)

# Cara Ketiga
string_5 = string_3.replace("mahasiswa RKA", "bukan mahasiswa RPL")
print(string_5)

# menghapus sebuah karakter di string kota asal
string_6 = string_2[0] + string_2[2] + string_2[-1]
print(string_6) #saya menghapus huruf vokal


# Escaping Sequencing

# Mencetak "Medan" dalam format Oktal
String_7 = "\115\145\144\141\156"
print("\nMencetak dalam Oktal dengan Escape Sequences: ")
print(String_7)

# Menggunakan raw string untuk mengabaikan escape sequences
String_7 = r"Saya berasal dari \115\145\144\141\156"
print("\nMencetak Raw String dalam Format Oktal: ")
print(String_7)

# Mencetak "Medan" dalam format Heksadesimal
String_7 = "Saya berasal dari \x4D\x65\x64\x61\x6E dalam HEX"
print("\nMencetak dalam HEX dengan Escape Sequences: ")
print(String_7)

# Menggunakan raw string untuk mengabaikan escape sequences
String_7 = r"Saya berasal dari \x4D\x65\x64\x61\x6E dalam \x48\x45\x58"
print("\nMencetak Raw String dalam Format HEX: ")
print(String_7)


# String Formating
print("--------------|Example_1|--------------")
# Default order
String1 = "{} {} {}".format('menyala', 'kota', 'medanku')
print("Print String in default order: ")
print(String1)

# Positional Formatting
String1 = "{2} {1} {0}".format('menyala', 'kota', 'medanku')
print("\nPrint String in Positional order: ")
print(String1)

# Keyword Formatting
String1 = "{m} {k} {c}".format(c='menyala', k='kota', m='medanku')
print("\nPrint String in order of Keywords: ")
print(String1)


print("--------------|Example_2|--------------")
# Formatting of Integers (Binary representation)
String1 = "{0:b}".format(10)
print("\nBinary representation of 10 is ")
print(String1)

# Formatting of Floats (Exponent representation)
String1 = "{0:e}".format(6062006.6458)
print("\nExponent representation of 6062006.6458 is ")
print(String1)

# Rounding off Floats
String1 = "{0:.2f}".format(3/4)
print("\ntiga per empat adalah : ")
print(String1)

print("--------------|Example_3|--------------")
# String alignment
String1 = "|{:<12}|{:^12}|".format('Kota', 'medan')
print("\nLeft, center and right alignment with Formatting: ")
print(String1)

# Aligning with additional spaces
String1 = "\n{0:^16} founded in {1:<4}!".format("Kota medan", 1590)
print(String1)


print("--------------|Example_4|--------------")
# Old Style Formatting of Floats
Integer1 = 10.082006
print("Formatting in 3.2f format: ")
print('Nilai dari Integer1 adalah %3.2f' % Integer1)

print("\nFormatting in 3.4f format: ")
print('Nilai dari Integer1 adalah %3.4f' % Integer1)