def binary_search(arr, target, low, high):
    if low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return binary_search(arr, target, mid + 1, high)
        else:
            return binary_search(arr, target, low, mid - 1)
    else:
        return -1

arr = list(input().split())
target = input()
result = binary_search(sorted(arr), target, 0, len(arr) - 1)
print(sorted(arr))
if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")