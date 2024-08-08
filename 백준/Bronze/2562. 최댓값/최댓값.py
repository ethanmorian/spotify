import sys

input = list(map(int, sys.stdin.read().strip().split('\n')))
print(max(input))
print(input.index(max(input))+1)