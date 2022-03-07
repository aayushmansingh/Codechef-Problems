n,k=list(map(int,input().split()))
l=[0]*n
for i in range(k):
    string=input()
    if string=="CLOSEALL":
        l=[0]*n
    elif string=="OPENALL":
        l=[1]*n
    else:
        no=int(string.split(' ')[1])
        if l[no-1]==1:
            l[no-1]=0
        else:
            l[no-1]=1
    print(l.count(1))
    