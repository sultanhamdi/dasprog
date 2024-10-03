# mencari total tarif per mile
value1 = float(input("odometer awal"))
value2 = float(input("odometer akhir"))
tarif = 1.5
traveled_distance = value2 - value1
traveled_distance = round(traveled_distance*tarif,3)
print("$",traveled_distance)