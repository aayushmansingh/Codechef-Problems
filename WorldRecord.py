# cook your dish here
import math
for tc in range(int(input())):
    k1,k2,k3,v=map(float,input().split())
    temp=k1*k2*k3*v
    res=100/temp
    print("yes" if round(res,2)<9.58 else "no")
    