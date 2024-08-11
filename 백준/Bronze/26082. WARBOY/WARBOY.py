import sys

print((lambda a, b, c: b//a*c*3)(*map(int, sys.stdin.read().strip().split())))