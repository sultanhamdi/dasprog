memo = {}

def SB(n):
    if n in memo:
        return memo[n]
    
    if n == 1:
        return 1
    
    if n % 2 == 0:
        memo[n]= 1 + SB(n/2)
        return memo[n]
    
    else:
        memo[n]= 1 + SB(n-1)
        return memo[n]

n = int(input()) 
print(SB(n))