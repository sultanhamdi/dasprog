#tampilan pilihan layanan gratis
print("(1) First Free Service")
print("(2) Second Free Service")

#input
service_number = int(input("Masukkan nomor layanan gratis>> "))
miles = int(input("Masukkan jumlah Mil>> "))

if service_number == 1:
    if 1500 <= miles <= 3000:
        print("Kendaraan harus diservis.")
    else:
        print("Kendaraan tidak perlu diservis.")
elif service_number == 2:
    if 3001 <= miles <= 4500:
        print("Kendaraan harus diservis.")
    else:
        print("Kendaraan tidak perlu diservis.")
else:
    print("Nomor layanan tidak valid. Silakan pilih 1 atau 2.")
