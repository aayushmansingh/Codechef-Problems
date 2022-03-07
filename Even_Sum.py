import math
test = 1
test = int(input())

for tc in range((test)):
    # Write your code....
    n = int(input())
    l = list(map(int, input().split()))
    sums = sum(l)
    print(1 if sums % 2 == 0 else 2)
