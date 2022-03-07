n=int(input())
l=list(map(int,input().split()))
sums=sum(l)
s=0
for i in range(1,n+1):
    s+=i
if s==sums:
    print('YES')
else:
    print('NO')
    