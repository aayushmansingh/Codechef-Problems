import math
test = 1
test = int(input())

for tc in range((test)):
    # Write your code....
    n = input()
    l = [x for x in n]
    res = ''
    if l[0] != '1':
        l.insert(0, '1')
        print(res.join(l))
        continue
    else:
        l.insert(1, '0')
        print(res.join(l))