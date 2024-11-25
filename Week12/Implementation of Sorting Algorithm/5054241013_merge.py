def merge_sort(N):
    if len(N) <= 1:
        return N

    mid = len(N) // 2
    left = merge_sort(N[:mid]) 
    right = merge_sort(N[mid:]) 

    i = j = 0
    sorted_arr = []
    
    # bandingin
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1

    # gabungin list
    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])

    return sorted_arr

N = [196418, 6765, 1597, 2584, 55, 2, 514229, 17711, 3, 46368, 28657, 0, 8, 34, 144, 
     317811, 2178309, 13, 1, 89, 832040, 1346269, 121393, 987, 377, 75025, 10946, 233, 
     4181, 21, 610, 5, 1]

print(merge_sort(N))
