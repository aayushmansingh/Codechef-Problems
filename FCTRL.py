# cook your dish here
T=int(input())
l=[]
for tc in range(T):
    l.append(int(input()))
for x in l:
    print(x//5+x//25+x//125+x//625+x//3125+x//15625+x//78125+x//390625+x//1953125+x//9765625+x//48828125+x//244140625)