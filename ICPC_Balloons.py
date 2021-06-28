import math
test = 1
test = int(input())

for tc in range((test)):
    # Write your code....
    colors = [1, 2, 3, 4, 5, 6, 7]

    n = int(input())
    l = list(map(int, input().split()))

    for i in l:
        if l[-1] in colors:
            print(n)
            break
        else:
            l.remove(l[-1])
            n -= 1
