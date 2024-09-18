def main():
    # Membaca input
    N, M, K = map(int, input().split())
    A = list(map(int, input().split()))
    
    # Membuat prefix sum untuk optimasi
    prefix_sum = [0] * (N + 1)
    for i in range(1, N + 1):
        prefix_sum[i] = prefix_sum[i - 1] + A[i - 1]

    total_energy_needed = 0

    # Proses setiap kasus
    for _ in range(K):
        X, Y = map(int, input().split())
        # Hitung energi yang dibutuhkan dari lantai X ke Y-1
        total_energy_needed += prefix_sum[Y - 1] - prefix_sum[X - 1]

    # Membandingkan dengan energi yang dimiliki
    if M >= total_energy_needed:
        print(f"EZ banget, energiku sisa {M - total_energy_needed}!")
    else:
        print(f"NT, kurang {total_energy_needed - M} energi sih.")

# Menjalankan fungsi utama
main()
