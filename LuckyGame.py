import math
test = 1
test = int(input())

for tc in range((test)):
    # Write your code....
    n = input()
    for i in n:
        if i != '3' and i != '7':
            print("BETTER LUCK NEXT TIME")
            break
    else:
        print("LUCKY")