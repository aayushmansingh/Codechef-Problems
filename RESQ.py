from math import sqrt
for tc in range(int(input())):
    n=int(input())
    mind=[]
    for i in range(1,int(sqrt(n))+1):
        if n%i==0:
            mind.append(abs(n//i-i))
    print(min(mind))