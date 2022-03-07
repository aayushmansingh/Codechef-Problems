for tc in range(int(input())):
    rounds=int(input())
    l=[0,0]
    for r in range(rounds):
        chef,morty=map(int,input().split())
        s1,s2=0,0
        while(chef>0):
            s1+=int(chef%10)
            chef//=10
        while(morty>0):
            s2+=int(morty%10)
            morty//=10
        if s1>s2:
            l[0]+=1
        elif s2>s1:
            l[1]+=1
        elif s1==s2:
            l[0]+=1
            l[1]+=1
    if l[0]>l[1]:
        print(0,l[0])
    elif l[1]>l[0]:
        print(1,l[1])
    else:
        print(2,l[0])