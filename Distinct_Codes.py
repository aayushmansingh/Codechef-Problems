import math
test = 1
test = int(input())

for tc in range((test)):
    # Write your code....
    s = input()
    freq = []
    for i in range(len(s) - 1):
        new = s[i] + s[i + 1]
        if new not in freq:
            freq.append(new)
    print(len(freq))