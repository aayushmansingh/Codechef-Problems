def prime(x):
    for i in range(2,x):
        if x%i==0:
            return False
            break
        
    else:
        return True 

T=int(input())
for tc in range(T):
    x,y=map(int,input().split())
    s=x+y
    number=1
    s+=1
    while not prime(s):
        s+=1
        number+=1
    print(number)