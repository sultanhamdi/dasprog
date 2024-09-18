def caesar_cipher(text, K):
    encrypted = ""
    for char in text:
        if char.isalpha():  # Mengecek apakah char adalah huruf
            base = ord('A') if char.isupper() else ord('a')
            encrypted += chr((ord(char) - base + K) % 26 + base)
        else:
            encrypted += char  # Jika bukan huruf, tambahkan apa adanya
    return encrypted

# Langkah 1: Ambil input angka di baris pertama
method, K = map(int, input("Masukkan metode dan K (misal '2 68'): ").split())

# Langkah 2: Ambil input string di baris berikutnya
text = input("Masukkan string yang akan diproses: ")

# Langkah 3: Pilih metode berdasarkan input angka pertama
if method == 2:
    # Jika metode 2, gunakan Caesar Cipher dengan rotasi besar, modulo 26
    K = K % 26  # Rotasi sebesar 68 mod 26 = 16
    result = caesar_cipher(text, K)
else:
    result = "Metode tidak dikenali"

# Langkah 4: Tampilkan hasil enkripsi
print(result)
