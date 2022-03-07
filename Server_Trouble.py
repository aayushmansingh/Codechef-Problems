import math
test = 1
test = int(input())

for tc in range((test)):
    # Write your code....
    n, k = map(int, input().split())
    if n % k == 0:
        print(n // k, k)
    else:
        d = (n // k) + 1
        pairs = n - (n // k) * k
        print(d, pairs)
