import sys

input = list(map(int, sys.stdin.read().strip().split()))

for i in sorted(input[1:]):
    print(i)