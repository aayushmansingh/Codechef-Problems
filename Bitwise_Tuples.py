#Problem Link: https://www.codechef.com/JUNE21C/problems/BITTUP

import math
test = 1
test = int(input())

for tc in range((test)):
    # Write your code....
    a, b = map(int, input().split())
    temp = 1000000007
    c = pow(2, a, temp) - 1
    print(pow(c, b, temp))
