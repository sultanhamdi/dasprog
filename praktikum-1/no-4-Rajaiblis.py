#input
U = int(input(""))
K = int(input(""))
M = int(input(""))

#freeze penyihir
M = M // 2
K = K // 2

#stats
dmg_raja = 100 * 10
dmg_minion = M * 2
dmg_knight = K * 5 * 5
hp_raja = 1000
hp_minion =100
hp_knight =500
total_dmg = dmg_knight + dmg_minion + dmg_raja
sisa_darah = U - total_dmg

if sisa_darah > 0 :
    print(f"Yey! Ucup Menang! HP tersisa: {sisa_darah}")

else:
    print("Yah! Ucup Meninggoy.")

    