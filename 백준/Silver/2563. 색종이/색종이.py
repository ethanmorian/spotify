import sys

r = []

for _ in range(int(sys.stdin.readline().strip())):
    w, h = map(int, sys.stdin.readline().strip().split())
    for i in range(w, w+10):
        for j in range(h, h+10):
            if [i,j] not in r:
                r.append([i,j])
    
print(len(r))