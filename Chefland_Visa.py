import math
test = 1
test = int(input())

for tc in range((test)):
    # Write your code....
    x1, x2, y1, y2, z1, z2 = map(int, input().split())
    if x2 >= x1 and y2 >= y1 and z2 <= z1:
        print("YES")
    else:
        print("NO")