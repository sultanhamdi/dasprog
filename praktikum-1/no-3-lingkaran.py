# Input data
x1, y1 = map(int, input().split())
xs, ys = map(int, input().split())
xf, yf = map(int, input().split())

jarak_total_kuadrat = (xf - xs) ** 2 + (yf - ys) ** 2

jarak_awal_center_kuadrat = (xs - x1) ** 2 + (ys - y1) ** 2

jarak_akhir_center_kuadrat = (xf - x1) ** 2 + (yf - y1) ** 2

if jarak_awal_center_kuadrat <= 0 or jarak_akhir_center_kuadrat <= jarak_total_kuadrat:
    print("No")
else:
    print("Yes")
