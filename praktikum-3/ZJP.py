import sys
sys.setrecursionlimit(10 ** 9)

# mas saya yang kebiasaan make memo jadi saya pake aja
memo = {}

def ZJP(n):
    
    if n in memo:
        return memo[n]
    
    if n == 0:
        return 0
    
    if n == 1:
        return 0
    
    if n == 2:
        return 1
    
    if n == 3:
        return 1
    
    if n == 4:
        return 2
    
    if n == 5:
        return 2
    
    if n == 6:
        return 4
    
    if n == 7:
        return 5
    
    if n == 8:
        return 8
    
    else:
        memo[n] = ((ZJP(n-2) + ZJP(n-3) + ZJP(n-4)) % 1000000007)
        return memo[n] 

n = int(input())
print(ZJP(n))