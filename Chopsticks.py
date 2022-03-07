n,d=map(int,input().split())
l=[]
for i in range(n):
    l.append(int(input()))
l.sort()
count=0
i=0
while(i<n-1):
    if l[i]+d>=l[i+1]:
        count+=1
        i+=2
    else:
        i+=1
print(count)