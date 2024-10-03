# Mencetak "Medan" dalam format Oktal
String1 = "\115\145\144\141\156"
print("\nMencetak dalam Oktal dengan Escape Sequences: ")
print(String1)

# Menggunakan raw string untuk mengabaikan escape sequences
String1 = r"Saya berasal dari \115\145\144\141\156"
print("\nMencetak Raw String dalam Format Oktal: ")
print(String1)

# Mencetak "Medan" dalam format Heksadesimal
String1 = "Saya berasal dari \x4D\x65\x64\x61\x6E dalam HEX"
print("\nMencetak dalam HEX dengan Escape Sequences: ")
print(String1)

# Menggunakan raw string untuk mengabaikan escape sequences
String1 = r"Saya berasal dari \x4D\x65\x64\x61\x6E dalam \x48\x45\x58"
print("\nMencetak Raw String dalam Format HEX: ")
print(String1)
