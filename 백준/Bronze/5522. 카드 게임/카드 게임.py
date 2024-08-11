import sys

print((lambda a: sum([*a]))(map(int, sys.stdin.read().strip().split('\n'))))