T = int(input())
N = list(map(int, input().split()))

max_harga = max(N)
frekuensi = [0] * (max_harga + 1)

for i in N:
    frekuensi[i] += 1

max_frekuensi = 0
modus = 0

for i in range(max_harga + 1):
    if frekuensi[i] > max_frekuensi:
         max_frekuensi = frekuensi[i]
         modus = i
    elif frekuensi[i] == max_frekuensi and i > modus:
        modus = i

prima = True
if modus < 2:
    prima = False
else:
    for i in range(2, int(modus**0.5)+1):
        if modus % i == 0:
            prima = True
            break

print(f"Modus: {modus}")
if prima:
    print("Wah, modenya prima nihh")
else:
    print("Yah, modenya gak prima")