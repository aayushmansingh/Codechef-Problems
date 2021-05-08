import math
test = 1
test = int(input())

for tc in range((test)):
    # Write your code....
    n=int(input())
    l=list(map(int,input().split()))
    sums=sum(l)
    minimum=min(l)
    ans=sums-minimum*n
    print(ans)