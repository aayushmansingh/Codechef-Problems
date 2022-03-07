for tc in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    c=0
    for i in range(n-1):
        c=c+(abs(l[i]-l[i+1])-1)
    print(c)