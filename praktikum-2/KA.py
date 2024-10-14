t = int(input())
for x in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    q = int(input())

    if q==1:
        newMax = float("-inf")
        for i in range(n):
            currSum = 0
            for j in range(i, min(i + k, n)):
                currSum += arr[j]
                newMax = max(newMax, currSum)
        print(newMax)
        
    elif q==2:
        newMin = float("inf")
        for i in range(n):
            currSum = 0
            for j in range(i, min(i + k, n)):
                currSum += arr[j]
                newMin = min(newMin, currSum)
print(newMin)