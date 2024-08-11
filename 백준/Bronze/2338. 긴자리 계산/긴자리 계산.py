import sys

print((lambda a, b: f'{a+b}\n{a-b}\n{a*b}')(*map(int, sys.stdin.read().strip().split('\n'))))