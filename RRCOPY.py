# cook your dish here
T=int(input())
for tc in range(T):
    n=int(input())
    l=[]
    l=list(map(int,input().split()))
    print(len(set(l)))