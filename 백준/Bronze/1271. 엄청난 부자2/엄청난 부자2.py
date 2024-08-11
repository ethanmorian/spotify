import sys

print((lambda n, m: f'{n//m}\n{n%m}')(*map(int, sys.stdin.read().strip().split())))