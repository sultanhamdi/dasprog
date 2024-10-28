N, M = map(int, input().split())
matrix = []

for i in range(N):
    a = input()
    k = []
    for i in a:
        k.append(int(i))
    matrix.append(k)
    
#print(matrix)
count = 0
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 1:
            if i-1>=0 and matrix[i-1][j] == 0:
                count += 1
            if i+1 < N and matrix[i+1][j] == 0:
                count += 1
            if j-1>=0 and matrix[i][j-1] == 0:
                count += 1
            if j+1 < M and matrix[i][j+1] == 0:
                count += 1
            if i-1 >= 0 and j-1 >= 0 and matrix[i-1][j-1] == 0:
                count += 1
            if i+1 < N and j+1 < M and matrix[i+1][j+1] == 0:
                count += 1
            if j-1 >= 0 and i+1 < N and matrix[i+1][j-1] == 0:
                count += 1
            if j+1 < M and i-1 >= 0 and matrix[i-1][j+1] == 0:
                count += 1

print(count)