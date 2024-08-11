import sys

print((lambda a, b: (a+b)*(a-b))(*map(int, sys.stdin.read().strip().split())))