# Logika utama untuk enkripsi atau dekripsi
mode, key = map(int, input().split())
pesan = input().lower()  # Memasukkan pesan
alphabet = "abcdefghijklmnopqrstuvwxyz"  # Alfabet untuk penggeseran

def Enkripsi(pesan, key, alphabet):
    shifted = alphabet[key % 26:] + alphabet[:key % 26]  # Membuat alfabet yang digeser
    encrypted = ""  # Menyimpan pesan yang telah dienkripsi
    for huruf in pesan:
        if huruf in alphabet:
            encrypted += shifted[alphabet.index(huruf)]  # Enkripsi dengan menggeser huruf
        else:
            encrypted += huruf  # Biarkan spasi dan simbol tetap sama
    return encrypted

def Dekripsi(pesan, key, alphabet):
    shifted = alphabet[-key % 26:] + alphabet[:-key % 26]  # Geser balik untuk dekripsi
    decrypted = ""  # Menyimpan pesan yang telah didekripsi
    for huruf in pesan:
        if huruf in alphabet:
            decrypted += shifted[alphabet.index(huruf)]  # Dekripsi dengan menggeser huruf kembali
        else:
            decrypted += huruf  # Biarkan spasi dan simbol tetap sama
    return decrypted


if mode == 1:
    result = Enkripsi(pesan, key, alphabet)  # Enkripsi pesan
elif mode == 2:
    result = Dekripsi(pesan, key, alphabet)  # Dekripsi pesan
else:
    result = "invalid"

print(result)
