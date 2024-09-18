def print_cake(N):
    if N <= 8:
        print("Too Small")
        return
    
    # Bagian atas kue (candle)
    print(' ' * (N//2) + '*')
    
    # Batang lilin (5 baris)
    for _ in range(4):
        print(' ' * (N//2 - 1) + '|-|')
    
    # Garis pemisah pertama
    print('-' * N)
    
    # Layer 1 (Lebar N//2), 4 baris
    layer1_width = N // 2 + 1
    for _ in range(4):
        print(' ' * ((N - layer1_width) // 2) + '|' + '=' * layer1_width + '|')
    
    # Garis pemisah kedua
    print('-' * (N + 1))  # Lebar bertambah sesuai contoh
    
    # Layer 2 (Lebar N//2 + 2), 4 baris
    layer2_width = (N // 2) + 3
    for _ in range(4):
        print(' ' * ((N - layer2_width) // 2) + '|' + '=' * layer2_width + '|')
    
    # Garis pemisah ketiga
    print('-' * (N + 2))  # Lebar bertambah lagi sesuai contoh

# Contoh penggunaan
N = int(input("Masukkan ukuran kue: "))
print_cake(N)
