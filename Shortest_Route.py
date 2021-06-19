import math
from os import sep
test = 1
test = int(input())

for tc in range((test)):
    # Write your code....
    n, m = map(int, input().split())
    an = []
    bn = []
    an = list(map(int, input().split()))
    bn = list(map(int, input().split()))
    ones, twos = -1, -1
    max = 1000000000
    l1 = []
    l2 = []

    for i in range(n):
        if an[i] == 1:
            l1.append(0)
            ones = i
        elif ones == -1:
            l1.append(max)
        elif an[i] == 2:
            l1.append(0)
        else:
            l1.append(i - ones)

    for i in range(n - 1, -1, -1):
        if an[i] == 2:
            l2.append(0)
            twos = i
        elif twos == -1 and an[i] == 0:
            l2.append(max)
        elif an[i] == 1:
            l2.append(0)
        else:
            l2.append(twos - i)
    reversed(l2)

    for i in range(m):
        temp = bn[i]
        if an[0] != 0 and an[temp - 1] != 0:
            print(0, end=' ')
        elif temp == 1:
            print(0, end=' ')
        else:
            res = 0
            if l1[temp - 1] == max and l2[temp - 1] == max:
                res = -1
            else:
                res = min(l1[temp - 1], l2[temp - 1])
                print(res, end=' ')
