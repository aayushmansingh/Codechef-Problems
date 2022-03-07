for tc in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    min=999999
    for i in l:
        if min>i:
            min=i
    print(min*(n-1))