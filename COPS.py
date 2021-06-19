#Problem Link: https://www.codechef.com/problems/COPS

for tc in range(int(input())):
    m,x,y=list(map(int,input().split()))
    loc=list(map(int,input().split()))
    product=x*y
    ans=[]
    for house in loc:
        a=house+product
        b=house-product
        if a>100:
            a=100
        if b<1:
            b=1
        for i in range(b,a+1):
            ans.append(i)
    ans=set(ans)
    print(100-len(ans))
