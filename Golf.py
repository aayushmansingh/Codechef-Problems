import math
test = 1
test = int(input())

for tc in range((test)):
    # Write your code....
    n,x,k=map(int,input().split())
    n+=1
    if x%k==0:
        print("YES")
    elif ((n-x)%k==0):
        print("YES")
    else:
        print("NO")