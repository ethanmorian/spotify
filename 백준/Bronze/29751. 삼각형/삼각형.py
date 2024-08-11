import sys

print((lambda w, h: w*h/2)(*map(int, sys.stdin.read().strip().split())))