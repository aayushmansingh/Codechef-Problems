import math
test = 1
test = int(input())

for tc in range((test)):
    # Write your code....
    D, d, P, Q = map(int, input().split())
    x = D // d
    if D % d == 0:
        ans = d * x * P + (Q * (x - 1) * x * d // 2)
        print(ans)
    else:
        ans = d * x * P + (Q * (x - 1) * x * d // 2)
        rem = D % d
        ans += rem * (P + x * Q)
        print(ans)