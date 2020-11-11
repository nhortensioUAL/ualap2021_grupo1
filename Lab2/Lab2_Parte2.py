def fatorial(n):
    if(n==1):
        return 1   
    else:
        return n*fatorial(n-1)
        
for i in range(1,20 + 1):
    print(fatorial(i))