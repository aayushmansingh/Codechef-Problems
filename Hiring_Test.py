t = int(input())
for tc in range(t):
    n, m = map(int, input().split())
    x, y = map(int, input().split())
    for i in range(n):
        ans = input()
        if (ans.count('F') >= x
                or (ans.count('F') == (x - 1) and ans.count('P') >= y)):
            print(1, end='')
        else:
            print(0, end='')
    print()