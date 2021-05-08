import random
a,b=map(int,input().split())
c=a-b
copy=c
d=c%10  #last digit
if d==9:
    c-=1  
else:
    c+=1
print(c)