import math
test = 1
test = int(input())

for tc in range((test)):
    # Write your code....
    n, k = map(int, input().split())
    l = list(map(int, input().split()))
    bit = [0] * 32
    for i in range(32):
        for item in l:
            if item & (1 << i):
                bit[i] += 1
    sum = 0
    for item in bit:
        sum += math.ceil(item / k)
    print(sum)