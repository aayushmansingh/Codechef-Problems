import math
test = 1
test = int(input())

for tc in range((test)):
    # Write your code....
    n = int(input())
    a = list(map(int, input().split()))
    c = 0
    for i in range(n):
        sum, pro = 0, 1
        for j in range(i, -1, -1):
            sum += a[j]
            pro *= a[j]
            if sum == pro:
                c += 1
    print(c)