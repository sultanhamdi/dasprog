Section = 30
Total_student = int(input("Masukkan jumlah siswa ="))

Filled_section = Total_student // Section
Leftover_student = Total_student % Section

print("number of sections", Filled_section)
print(Leftover_student,"left over students")