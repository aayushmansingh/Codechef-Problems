# cook your dish here
try:
    tc = int(input())
    while (tc):
        D, d, a, b, c = map(int, input().split())
        res = D * d
        if res < 10:
            print(0)
            continue
        if res >= 10 and res < 21:
            print(a)
            continue
        if res > 10 and res < 42:
            print(b)
            continue
        if res > 10 and res > 42:
            print(c)
            continue
        tc -= 1
except:
    pass
