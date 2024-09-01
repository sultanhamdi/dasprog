#input volume infuse
volume = float(input("Volume to be infused (ml) =>"))
round(volume,2)

#input waktu dalam menit
Minute = float(input("Minutes over which to infuse =>"))
round(Minute,2)

#mengubah ke jam
Hours = Minute /60

#output
print("VTBI:", volume, "ml")
print("Rate:", volume/Hours,"ml/hr")