n=int(input())
c=0
while(n>0):
    d=n%10
    c+=1
    n//=10
if c==1:
    print(1)
if c==2:
    print(2)
if c==3:
    print(3)
if c>3:
    print("More than 3 digits")