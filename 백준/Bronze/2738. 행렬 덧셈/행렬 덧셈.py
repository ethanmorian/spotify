import sys

n, m = map(int, sys.stdin.readline().split())

a = [list(map(int, sys.stdin.readline().split())) for line in range(n)]
b = [list(map(int, sys.stdin.readline().split())) for line in range(n)]

for i in range(n):
    result = []
    for j in range(m):
        result.append(a[i][j] + b[i][j])
    print(' '.join(map(str, result)))