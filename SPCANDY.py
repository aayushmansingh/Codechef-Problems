n=int(input())
for tc in range(n):
    n,k=map(int,input().split())
    if k==0:
        print(0,n)
    else:
        print(n//k,n%k)