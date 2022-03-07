import math
for tc in range(int(input())):
    n,m,k=map(int,input().split())
    while(n<m and k>0):
        n+=1
        k-=1
    while(m<n and k>0):
        m+=1 
        k-=1 
    if m==n:
        print(m-n)
    elif m>n:
        print(m-n)
    else:
        print(n-m)