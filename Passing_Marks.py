test = int(input())

while (test):
    # Write your code....
    amin, bmin, cmin, tmin, a, b, c = [int(x) for x in input().split()]
    if (a >= amin and b >= bmin and c >= cmin and (a + b + c) >= tmin):
        print("YES")
    else:
        print("NO")
    test -= 1
