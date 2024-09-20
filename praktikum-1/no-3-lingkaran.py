x1, y1 = map(int(input().split()))
xs, ys = map(int(input().split()))
xf, yf = map(int(input().split()))

jarak_total = ((xf - xs) ** 2 + ((yf - ys) ** 2) ** 0,5)
langkah = int(jarak_total)
jarak_awal_center = ((xs - x1) ** 2 + ((ys - y1) ** 2) ** 0.5)
jarak_akhir_center = ((xf - x1) ** 2 + ((yf - y1) ** 2) ** 0.5)

if jarak_awal_center <= 0 or jarak_akhir_center <= langkah:
    print("No")
else:
    print("Yes")
