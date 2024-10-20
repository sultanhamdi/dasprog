arr = list(map(int, input().split()))

frekuensi = {}
for i in arr:
    frekuensi.update({i : arr.count(i)})
# print(frekuensi)

max_value = max(frekuensi.values())
# print(max_value)

daftarModus = []
for key, value in frekuensi.items():
    if value == max_value:
        daftarModus.append(key)
print(daftarModus)

if len(daftarModus) == 1 :
    print(f"{daftarModus}*{max_value}={daftarModus*max_value} ")