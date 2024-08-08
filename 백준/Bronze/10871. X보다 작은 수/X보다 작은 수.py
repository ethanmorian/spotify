import sys

input = sys.stdin.read().strip().split('\n')
x = int(input[0].split()[1])
print(' '.join([str(i) for i in map(int, input[1].split()) if i < x]))