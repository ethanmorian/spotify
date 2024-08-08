import sys

input = sys.stdin.read().strip().split('\n')

print(sum(int(i)for i in input[1]))
