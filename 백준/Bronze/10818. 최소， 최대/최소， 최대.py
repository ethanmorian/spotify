import sys

input = sys.stdin.read().strip().split('\n')
print(min(map(int, input[1].split())), max(map(int, input[1].split())))