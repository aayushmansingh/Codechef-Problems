import math
test=1
test=int(input())
def power(x, y, mod):
    res = 1
    x=x%mod
    if x==0:
            return 0

    while (y > 0):
            if y&1:
                    res=(res*x)%mod
            y=y//2
            x=(x*x)%mod
    return res
for tc in range((test)):
        #Write your code....
        n=int(input())
        print(power(2,n-1,1000000007))