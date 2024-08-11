import sys

n, a, b = map(int, sys.stdin.read().strip().split())

if a < b:
    print('Bus')
elif a > b:
    print('Subway')
else:
    print('Anything')