import sys

print((lambda a, b: f'{b-a} {b}')(*map(int, sys.stdin.read().strip().split())))