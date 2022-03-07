n = int(input())
for tc in range(n):
    a, b, c, d = map(int, input().split())
    print(c // a + d // b)
