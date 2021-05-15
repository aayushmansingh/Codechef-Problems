import math
test=1
test=int(input())

for tc in range((test)):
        #Write your code....
        a,b,c=map(int,input().split())
        ans=(b+(100-a)*c)*10
        print(ans)