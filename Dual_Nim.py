import math
test = 1
test = int(input())

for tc in range((test)):
    # Write your code....
    n = int(input())
    l = list(map(int, input().split()))
    val = 0
    for i in range(n):
        val = val ^ l[i]
    if val == 0:
        print("First")
    elif n % 2 == 0:
        print("First")
    else:
        print("Second")
