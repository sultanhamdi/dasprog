S = input("")  
N = len(S)  
palindrome = True

if S == S[::-1]:
    print("Palindrome King!")  
else:
    print("Bukan King!")