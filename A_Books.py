test = int(input())

for _ in range(test):
    n = int(input())
    l = list(map(int, input().split()))
    res = []
    for i in range(n):
        c = 0
        for j in range(i, n):
            if l[j] > l[i]:
                c += 1
        res.append(c)
    print(*res)