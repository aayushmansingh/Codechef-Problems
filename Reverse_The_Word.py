string=input().split(' ')
s1=string[0]
new=''
for i in reversed(s1):
    new+=i
print(new,end=' ')
print(' '.join(string[1:]))