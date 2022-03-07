try:
    t = int(input())
    while t>0:
        (D,d,a,b,c) = map(int,input().split(" "))
        r = D*d;
        if(r<10):
            print(0)
        elif(r>=10 and r<21):
            print(a)
        elif(r>=21 and r<42):
            print(b)
        else:
            print(c)
        t = t-1 
except:
    pass