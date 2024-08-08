import sys

m = 0

for i in range(9):
    line = list(map(int, sys.stdin.readline().split()))
    for j in range(9):
        if m <= line[j]:
            m = line[j]
            r, c = i, j
print(f"{m}\n{r+1} {c+1}")