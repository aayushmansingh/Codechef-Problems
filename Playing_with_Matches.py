match = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
n = int(input())
for tc in range(n):
    a, b = map(int, input().split())
    sums = a + b
    res = 0
    while (sums > 0):
        d = sums % 10
        res += match[d]
        sums //= 10
    print(res)