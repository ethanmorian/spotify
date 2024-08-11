import sys

print((lambda n, m: 'Yes' if n*100 >= m else 'No')(*map(int, sys.stdin.read().strip().split())))