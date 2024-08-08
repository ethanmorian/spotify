import sys

vps = sys.stdin.read().splitlines()[1:]

result = []

for i in vps:
    stack = []
    for j in i:
        if j == ")" and "(" in stack:
            stack.remove("(")
        else:
            stack.append(j)
            
    if len(stack) == 0:
        result.append("YES")
    else:
        result.append("NO")
        
print("\n".join(result))