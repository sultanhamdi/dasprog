U = int(input("Masukkan HP Ucup: "))  
M = int(input("Masukkan jumlah Minion Ibis: "))  
K = int(input("Masukkan jumlah Knight Ibis: "))  
def can_ucup_win(U, M, K):  
    # Menghitung total damage yang diterima Ucup  
    damage_minion = M  # Damage dari Minion (M/2 * 2 = M)  
    damage_knight = (5 * K) / 2  # Damage dari Knight (K/2 * 5 = 5K/2)  
    damage_raja_ibis = 100  # Damage dari Raja Ibis  

    # Total Damage  
    total_damage = damage_minion + damage_knight + damage_raja_ibis  
    
    # Mengecek apakah Ucup bisa bertahan  
    can_win = U > total_damage  
    sisa = U - total_damage
    return can_win  

# Meminta input dari pengguna  

if can_ucup_win(U, M, K):  
    print(f"Yey! Ucup Menang! HP tersisa: {sisa_darah}")

else:  
    print("Yah! Ucup Meninggoy.")