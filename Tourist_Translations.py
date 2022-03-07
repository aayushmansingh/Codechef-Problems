import math
n, string = input().split()
string = list(string)

for i in range(int(n)):
    convo = list(input())
    ans = []
    for j in convo:
        if j == '_':
            char = ' '
            ans.append(char)
        elif ord(j.lower()) >= ord('a') and ord(j.lower()) <= ord('z'):
            char = string[ord(j.lower()) - 97]
            if j.isupper() == True:
                ans.append(char.upper())
            else:
                ans.append(char)
        else:
            ans.append(j)
    print(''.join(ans))
