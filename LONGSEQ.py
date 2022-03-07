import math
test=1
test=int(input())

for tc in range((test)):
        #Write your code....
        c1=0
        c0=0
        n=input()
        for i in n:
                if i=='1':
                        c1+=1
                elif i=='0':
                        c0+=1
        if c1==1 or c0==1:
                print("Yes")
        else:
                print("No")