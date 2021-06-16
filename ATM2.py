#Problem Link: https://www.codechef.com/problems/ATM2

import math
test=1
test=int(input())

for tc in range((test)):
        #Write your code....
        n,k=map(int,input().split())
        l=list(map(int,input().split()))
        res=[]
        for i in l:
                if i<=k:
                        res.append(1)
                        k-=i
                else:
                        res.append(0)
        for i in res:
                print(i,sep='', end='')
        print()
