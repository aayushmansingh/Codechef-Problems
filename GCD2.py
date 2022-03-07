# cook your dish here
def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
T=int(input())
for tc in range(T):
    x,y=map(int,input().split())
    print(gcd(x,y))
