def fibonacci_sequence(n):
    if n == 0:
        return [0]
    elif n == 1:
        return [0, 1]
    
    sequence = [0, 1]
    for i in range(2, n + 1):
        next_term = sequence[-1] + sequence[-2]
        sequence.append(next_term)
    
    return sequence

n = int(input())
result = fibonacci_sequence(n)
print(result)
