a, b = map(int, input().split())

if a % b == 0:
    c = b
elif b % a == 0:
    c = a
elif a > b:
    if a % b != 0:
        c = a % b
    else:
        c = b
else:  # b > a
    if b % a != 0:
        c = b % a
    else:
        c = a
d = (a * b) // c

#seharusnya hasil = ((c*d)/a)+((c*d)/b)

hasil = a + b
print(int(hasil))