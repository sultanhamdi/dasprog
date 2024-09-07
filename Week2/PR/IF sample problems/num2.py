#input
berat = float(input("Masukkan berat badan Anda dalam pound: "))
tinggi = float(input("Masukkan tinggi badan Anda dalam inci: "))

#rumus
bmi = (703 * berat) / (tinggi ** 2)

#Mengkategorikan
if bmi < 18.5:
    kategori = "Underweight"
elif 18.5 <= bmi <= 24.9:
    kategori = "Normal"
elif 25.0 <= bmi <= 29.9:
    kategori = "Overweight"
else:
    kategori = "Obese"

#output
print(f"\nBMI Anda adalah {bmi:.1f}, yang berarti Anda termasuk dalam kategori: {kategori}.")
