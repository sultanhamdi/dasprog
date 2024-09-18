#input
U = int(input(""))
K = int(input(""))
M = int(input(""))

#stats
jumlah_monster = M + K + 1

jumlah_attack_minion = (K/2) * 2
jumlah_health_minion = K * 100

jumlah_attack_knight = (M/2) * 5
jumlah_health_knight = M * 500

attack_king = 100
health_king = 1000

attack_ucup = 100 * jumlah_monster
health_ucup = U

jumlah_darah_musuh = jumlah_health_minion + jumlah_health_knight + health_king
banyak_serang = jumlah_darah_musuh // attack_ucup
dmg_musuh = jumlah_attack_minion + jumlah_attack_knight + attack_king
sisa_darah = U -(banyak_serang * dmg_musuh)

if sisa_darah > 0 :
    print(f"Yey! Ucup Menang! HP tersisa: {sisa_darah}")

else:
    print("Yah! Ucup Meninggoy.")

    