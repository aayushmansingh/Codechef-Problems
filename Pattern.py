n = int(input())
for tc in range(n):
    p = int(input())
    for i in range(1, p + 1):
        for j in range(1, i + 1):
            print(j, end='')
            if j != i:
                print("*" * j, end='')
        print()