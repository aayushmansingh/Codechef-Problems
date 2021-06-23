import math
test = 1
test = int(input())

for tc in range((test)):
    # Write your code....
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()
    c = 1
    res = 0
    for i in range(n - 1, -1, -1):
        if c % 2 == 1:
            res += l[i]
        c += 1
    print(res)