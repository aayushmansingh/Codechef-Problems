t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    l = list(map(int, input().split()))
    l.sort(reverse=True)
    m = 0
    o = 0
    sum1 = 0
    sum2 = 0
    d = 0
    for i in range(n):
        if (m < k):
            sum1 += l[2 * i]
            m += 1
        if (o <= k):
            if (o < (k - 1)):
                sum2 += l[(2 * i) + 1]
            if (o == (k - 1)):
                sum2 += l[(2 * i) + 1] + l[(2 * i) + 2]
                break
            o += 1
    d = max(sum1, sum2)
    print(d)
