def prime(n) : 
    if (n <= 1) :  
        return False
    if (n <= 3) :  
        return True
    if (n % 2 == 0 or n % 3 == 0) :  
        return False

    i = 5
    while(i * i <= n) :  
        if (n % i == 0 or n % (i + 2) == 0) :  
            return False
        i = i + 6
    return True

n = int(input())
li = []
count = 1
i = 2
while count <= n:
    if prime(i):
        li.append(i)    
        count += 1
    i+=1
print(sum(li))
