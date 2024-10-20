N = int(input())

for i in range(2 * N + 1):
    num_range = N - abs(N - i)
    
    # Print leading spaces for centering
    print(' ' * (N - num_range) * 2, end='')

    # Print the increasing part of the row
    for j in range(num_range + 1):
        print(j, end=' ')

    # Print the decreasing part of the row
    for j in range(num_range - 1, -1, -1):
        print(j, end=' ')

    # Move to the next line after finishing the row
    print()
