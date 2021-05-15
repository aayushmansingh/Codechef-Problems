for tc in range(int(input())):
    n=int(input())
    l=[100,50,10,5,2,1]
    sn=0
    i=0
    while(n!=0):
        if n>=l[i]:
            sn=sn+n//l[i]
            n=n%l[i]
        else:
            i+=1
    print(sn)