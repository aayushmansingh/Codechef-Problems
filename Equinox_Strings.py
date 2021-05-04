import math
test = 1
test = int(input())

for tc in range((test)):
    # Write your code....
    n,a,b=map(int,input().split())
    sarthak=0
    anuradha=0

    while(n>0):
        string=input()
        if string[0] in 'EQUINOX':
            sarthak+=a
        else:
            anuradha+=b
        n-=1
    if sarthak>anuradha:
        print("SARTHAK")
    elif anuradha>sarthak:
        print("ANURADHA")
    else:
        print("DRAW")
