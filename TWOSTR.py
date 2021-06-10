for tc in range(int(input())):
    x=input()
    y=input()
    for i in range(len(x)):
        if x[i]==y[i]:
            continue
        elif x[i]!=y[i]:
            if x[i]=='?' or y[i]=='?':
                continue
            else:
                print('No')
                break
    else:
        print('Yes')