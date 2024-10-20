t = int(input())
for x in range(t):
    n, k = map(int, input().split())
    bil = list(map(int, input().split()))
    q = int(input())

    if q == 1: # mencari maks
        newMax = float("-inf")
        for i in range(n):
            currSum = 0
            # Cek semua subarray yang dimulai dari i dengan panjang maksimal k
            for j in range(i, min(i + k, n)):
                currSum += bil[j]
                newMax = max(newMax, currSum)
        print(newMax)

    elif q == 2: # mencari min
        newMin = float("inf")
        for i in range(n):
            currSum = 0
            # Cek semua subarray yang dimulai dari i dengan panjang maksimal k
            for j in range(i, min(i + k, n)):
                currSum += bil[j]
                newMin = min(newMin, currSum)
        print(newMin)
