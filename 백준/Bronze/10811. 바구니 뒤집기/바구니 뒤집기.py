import sys

input = sys.stdin.read().strip().split('\n')

n, m = map(int, input[0].split())

baskets = list(range(1, n+1))

for line in input[1:]:
    i, j = map(int, line.split())
    baskets[i-1:j] = reversed(baskets[i-1:j])

print(' '.join(map(str, baskets)))