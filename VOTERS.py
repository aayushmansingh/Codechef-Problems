import collections
n1,n2,n3=map(int,input().split())
l1,l2,l3=[],[],[]
l4=[]
for i in range(n1+n2+n3):
    l4.append(int(input()))
freq={}
for item in l4:
    if item in freq:
        freq[item]+=1
    else:
        freq[item]=1
l5=[]
for key,value in freq.items():
    if value>=2:
        l5.append(key)
print(len(l5))
l5.sort()
for i in l5:
    print(i)