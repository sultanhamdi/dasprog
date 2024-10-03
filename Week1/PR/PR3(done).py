Hours = float(input("Masukkan jam"))
Minutes = float(input("Masukkan menit"))
Minutes = Minutes/60
Time = Hours + Minutes
t = Time
Temperature = (4 * t**2) / (t+2) - 20
print(Temperature,"C")