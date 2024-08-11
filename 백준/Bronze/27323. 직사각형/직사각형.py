import sys

print((lambda n, m: n*m)(*map(int, sys.stdin.read().strip().split('\n'))))