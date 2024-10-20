import statistics as st

inputan = input()
data = []

# konversi inputan ke dalam list yg berisi integer
for bilangan in inputan.split():
    data.append(int(bilangan))
# Menghitung modus
modus = st.mode(data)

# Menghitung frekuensi kemunculan modus
frekuensi_modus = data.count(modus)

hasil = modus * frekuensi_modus

# Menampilkan hasil
print(f'Data -> {data}')
print(f'Modus -> {modus}')
print(f'Modus muncul sebanyak -> {frekuensi_modus} kali')
print(f'Jawaban -> {hasil}')