T=int(input())
for tc in range(T):
    s=input()
    ca=0
    cb=0
    for i in s:
        if i=='a':
            ca+=1
        else:
            cb+=1
    if ca<=cb:
        print(ca)
    else:
        print(cb)