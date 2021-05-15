for tc in range(int(input())):
    n,k=map(int,input().split())
    s=list(map(str,input().split()))
    s=''.join(s)
    c=0
    for i in range(n):
        if s[i]=='*':
            c+=1
        else:
            if c>=k:
                break
            else:
                c=0
    if c>=k:
        print('yes')
    else:
        print('no')
    c=0