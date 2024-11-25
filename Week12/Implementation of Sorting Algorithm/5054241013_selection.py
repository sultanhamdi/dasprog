def selection(N):
   for i in range(len(N)):
      min_i = i
      for j in range(i + 1, len(N)):
         if N[min_i] > N[j]:
            min_i = j
      N[i], N[min_i] = N[min_i], N[i]
   return N

N = [196418, 6765, 1597, 2584, 55, 2, 514229, 17711, 3, 46368, 28657, 0, 8, 34, 144, 317811, 2178309, 13, 1, 89, 832040, 1346269, 121393, 987, 377, 75025, 10946, 233, 4181, 21, 610, 5, 1]
print(selection(N))
