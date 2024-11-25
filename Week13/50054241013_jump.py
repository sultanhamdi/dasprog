import math

def jump_search(arr, target):
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0
    while arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1
    while arr[prev] < target:
        prev += 1
        if prev == min(step, n):
            return -1
    if arr[prev] == target:
        return prev
    return -1

arr = list(map(int, input().split()))
target = int(input())
result = jump_search(sorted(arr), target)
print(sorted(arr))
if result != -1:
    print(f"Jump Search: Element found at index {result}")
else:
    print("Jump Search: Element not found")