import math
test = 1
test = int(input())

for tc in range((test)):
    # Write your code....
    n, k, v = map(int, input().split())
    l = list(map(int, input().split()))
    x = (v * (n + k) - sum(l))
    res = x % k
    if x <= 0 or res != 0:
        print(-1)
    else:
        print(x // k)
