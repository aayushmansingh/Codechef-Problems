# cook your dish here
n=int(input())
l=list(map(int,input().split()))
s1=sum(l)
q=int(input())
x=list(map(int,input().split()))
while(q>0):
    s1=(2*s1)%1000000007
    print(s1)
    q-=1