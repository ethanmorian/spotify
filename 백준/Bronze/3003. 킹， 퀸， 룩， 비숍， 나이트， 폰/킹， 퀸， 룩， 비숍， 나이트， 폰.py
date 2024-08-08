import sys

input = sys.stdin.read().strip().split()
print(' '.join(str(j-int(i)) for i, j in zip(input, [1, 1, 2, 2, 2, 8])))