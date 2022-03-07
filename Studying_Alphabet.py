s = input()
for i in range(int(input())):
    word = input()
    c = 0
    for j in word:
        if j in s:
            c += 1
    if c == len(word):
        print("Yes")
    else:
        print("No")
