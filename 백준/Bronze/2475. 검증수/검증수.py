import sys

print((lambda a, s, d, f, g: sum([a**2, s**2, d**2, f**2, g**2])%10)(*map(int, sys.stdin.read().strip().split())))