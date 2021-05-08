import math
test = 1
# test = int(input())

# for tc in range((test)):
    # Write your code....
def validate(string):
    stack_open=[]
    count=0
    for i in string:
        if i=='(' or i=='{' or i=='[':
            stack_open.append(i)
            count+=1
            continue
        if len(stack_open)==0:
            return count+1
        x=stack_open.pop()
        if i==')' and x=='(':
            count+=1
        elif i=='}' and x=='{':
            count+=1
        elif i==']' and x=='[':
            count+=1
        else:
            return count+1
    if len(stack_open)==0:
        return 0
    else:
        return count+1
s=input()
print(validate(s))