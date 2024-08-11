import sys

print((lambda t, s: '320' if 12 <= t <= 16 and s == 0 else '280')(*map(int, sys.stdin.read().strip().split())))