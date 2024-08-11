import sys

print((lambda n: f'{int(n * 0.78)} {int(n * 0.956)}')(*map(int, sys.stdin.read().strip().split())))