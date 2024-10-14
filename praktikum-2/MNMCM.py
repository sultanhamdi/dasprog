N = int(input())
arr = list(map(int,input().split()))

flag = 1
result = 1
for x in range(N):
    for y in range(x + 1, N):
        xor = arr[x]^arr[y]
        if xor == 0:
            result = 0
            flag = 0
            break
        else:
            result *= xor
    if flag == 0:
        break
print(result)