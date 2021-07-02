import math
test = 1
test = int(input())

for tc in range((test)):
    # Write your code....
    a, b, x = map(int, input().split())
    c = 0
    while (a < b):
        a += x
        c += 1
    print(c)
