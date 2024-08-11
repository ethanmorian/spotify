import sys

print((lambda a, b: '1' if a==b else '0')(*sys.stdin.read().strip().split()))