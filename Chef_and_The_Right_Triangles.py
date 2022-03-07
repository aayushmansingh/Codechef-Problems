n=int(input())
c=0
for i in range(n):
    x1,y1,x2,y2,x3,y3=map(int,input().split())
    line1=(y2-y1)**2+(x2-x1)**2
    line2=(y3-y1)**2+(x3-x1)**2
    line3=(y3-y2)**2+(x3-x2)**2
    
    l=[line1,line2,line3]
    l.sort()
    if l[0]+l[1]==l[2]:
        c+=1
print(c)