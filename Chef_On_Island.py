#Problem Link: https://www.codechef.com/problems/CCISLAND

import math
test = 1
test = int(input())

for tc in range((test)):
    # Write your code....
    x, y, xr, yr, d = map(int, input().split())
    res = min(x / xr, y / yr)
    if res >= d:
        print("YES")
    else:
        print("NO")
