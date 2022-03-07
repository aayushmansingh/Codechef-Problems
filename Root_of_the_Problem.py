import math
test = 1
test = int(input())

for tc in range((test)):
    # Write your code....
    n = int(input())
    res = 0
    for i in range(n):
        id, sum = map(int, input().split())
        res += (id - sum)
    print(res)