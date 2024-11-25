import time
def bubble(N):
    for i in range(len(N) - 1, 0, -1):
        for j in range(i):
            if N[j] > N[j + 1]:
                temp = N[j]
                N[j] = N[j + 1]
                N[j + 1] = temp
    return N

start_time = time.time() 
N = [196418, 6765, 1597, 2584, 55, 2, 514229, 17711, 3, 46368, 28657, 0, 8, 34, 144, 317811, 2178309, 13, 1, 89, 832040, 1346269, 121393, 987, 377, 75025, 10946, 233, 4181, 21, 610, 5, 1]
print(bubble(N))
end_time = time.time()
print(f"Runtime: {end_time - start_time:.6f} seconds")