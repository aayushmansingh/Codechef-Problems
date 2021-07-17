# Problem approach: https://youtu.be/Q_UX3Yrw-Bs

n = int(input())
for i in range(n):
    l, r = map(int, input().split())
    if r < 2 * l:
        print(r)
    else:
        print(-1)