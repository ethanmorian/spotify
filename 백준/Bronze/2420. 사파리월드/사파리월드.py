import sys

print((lambda a, b: abs(a-b))(*map(int, sys.stdin.read().strip().split())))