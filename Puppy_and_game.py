import math
test = 1
test = int(input())

for tc in range((test)):
    # Write your code....
    a, b = map(int, input().split())
    if a % 2 == 1 and b % 2 == 1:
        print("Vanka")
    else:
        print("Tuzik")