import math
test = 1
test = int(input())

for tc in range((test)):
    # Write your code....
    d, x, y, z = map(int, input().split())
    print(max(7 * x, y * d + z * (7 - d)))
