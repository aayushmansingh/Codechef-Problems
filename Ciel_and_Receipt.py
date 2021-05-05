import math
test = 1
test = int(input())

for tc in range((test)):
    # Write your code....
    p=int(input())
    l=[1,2,4,8,16,32,64,128,256,512,1024,2048]
    c=0
    i=11
    while(i>=0):
        if p>=l[i]:
            p=p-l[i]
            c+=1
            i+=1
        i-=1
    print(c)
