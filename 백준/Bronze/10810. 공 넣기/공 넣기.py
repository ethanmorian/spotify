import sys

input = sys.stdin.read().strip().split('\n')
basket, M = map(int, input[0].split())
result = [0 for _ in range(basket)]

for a in range(1, M+1):
    i, j, k = map(int, input[a].split())
    for index in range(i-1, j):
        result[index] = k

print(' '.join(map(str, result))) 