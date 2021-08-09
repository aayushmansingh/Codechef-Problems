for tc in range(int(input())):
    n=int(input())
    string=input()
    ct=0
    flag=0
    for i in range(n):
        ct+=int(string[i])-int('0')
        if 2*ct>=(i+1):
            flag=1
    if flag==1:
        print("YES")
    else:
        print("NO")