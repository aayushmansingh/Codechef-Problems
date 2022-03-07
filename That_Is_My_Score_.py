import math
test = 1
test = int(input())

for tc in range((test)):
    # Write your code....
    n = int(input())
    score = 0
    l = [0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(n):
        p, s = map(int, input().split())
        if p < 9:
            l[p - 1] = max(l[p - 1], s)
    print(sum(l))
