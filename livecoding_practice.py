arr = list(map(int, input().split()))

frekuensi = {}
for i in arr:
    frekuensi.update({i : arr.count(i)})
# print(frekuensi)

max_frekuensi = max(frekuensi.values())
# print(max_frekuensi)

daftarModus = []
for key, value in frekuensi.items():
    if value == max_frekuensi:
        daftarModus.append(key)
print(daftarModus)


# test case 1
if len(daftarModus) == 1:
    if len(daftarModus) == 1 :
        print(f"{daftarModus[0]}*{max_frekuensi}={daftarModus[0]*max_frekuensi} ")

# test case 2


# test case 3
elif len(arr) == 1:
    print(-1)