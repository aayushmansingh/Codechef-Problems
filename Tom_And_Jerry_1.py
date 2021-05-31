# cook your dish her
t = int(input())
for i in range(t):
    a, b, c, d, k = map(int, input().split())
    x = abs(c - a)
    y = abs(d - b)
    z = x + y
    if (k == z):
        print("yes")
    if (z > k):
        print("no")
    if ((k - z) % 2 == 1) and k > z:
        print("no")
    if ((k - z) % 2 == 0) and k > z:
        print("yes")