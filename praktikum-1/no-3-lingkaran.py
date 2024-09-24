# Input data
x1, y1 = map(int, input().split()) # Titik pusat lingkaran
xs, ys = map(int, input().split()) # Titik awal perjalanan King
xf, yf = map(int, input().split()) # Titik akhir (tujuan) perjalanan King

jarak_total_kuadrat = (xf - xs) ** 2 + (yf - ys) ** 2 #Menghitung Kuadrat Jarak Total dari Titik Awal ke Titik Akhir

jarak_awal_center_kuadrat = (xs - x1) ** 2 + (ys - y1) ** 2 #Menghitung Kuadrat Jarak dari Titik Awal ke Pusat Lingkaran

jarak_akhir_center_kuadrat = (xf - x1) ** 2 + (yf - y1) ** 2 #Menghitung Kuadrat Jarak dari Titik Akhir ke Pusat Lingkaran

if jarak_awal_center_kuadrat <= 0 or jarak_akhir_center_kuadrat <= jarak_total_kuadrat:
    print("No")
else:
    print("Yes")
