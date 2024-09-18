a, b = map(int, input().split())

if a == 0:  
    c = b  
elif b == 0:  
    c = a  
else:  
    if a > b:  
        if a % b == 0:  
            c = b  
        elif b % (a % b) == 0:  
            c = a % b  
        else:  
            c = 1  
    else:  # b >= a  
        if b % a == 0:  
            c = a  
        elif a % (b % a) == 0:  
            c = b % a  
        else:  
            c = 1  
d = (a * b) // c  

hasil = ((c*d)/a)+((c*d)/b)
print(hasil)