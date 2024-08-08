import sys

r = []

for _ in range(int(sys.stdin.readline().strip())):
    c = int(sys.stdin.readline().strip())
    parts = []
    
    for i in [25, 10, 5, 1]:
        parts.append(str(c // i))
        c = c % i
    
    tmp = " ".join(parts)
    r.append(tmp)
    
print("\n".join(r))