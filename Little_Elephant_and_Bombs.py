n = int(input())
while n:
    length = int(input())
    s = input()
    res = 0
    for i in range(length):
        if i == 0 and s[i] != '1' and s[i + 1] != '1':
            res += 1
        elif i == length - 1 and s[i] != '1' and s[i - 1] != '1':
            res += 1
        elif s[i] != '1' and s[i - 1] != '1' and s[i + 1] != '1':
            res += 1
    n -= 1
    print(res)