import math
for i in range(int(input())):
    p, s = map(int, input().split())
    v = (((p - (math.sqrt((p ** 2) - (24 * s)))) / 12) ** 2) * ((p / 4) - 2 * ((p - math.sqrt((p ** 2) - (24 * s))) / 12))
    print('{:.2f}\n'.format(v))