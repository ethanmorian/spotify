import sys

input = sys.stdin.read().splitlines()[1:]

stack = []

for i in input:
    if "push" in i:
        stack.append(i.split()[1])
    elif i == "pop":
        if len(stack) == 0:
            print("-1")
        else:
            print(stack.pop())
    elif i == "size":
        print(len(stack))
    elif i == "empty":
        if len(stack) == 0:
            print("1")
        else:
            print("0")
    elif i == "top":
        if len(stack) == 0:
            print("-1")
        else:
            print(stack[-1])