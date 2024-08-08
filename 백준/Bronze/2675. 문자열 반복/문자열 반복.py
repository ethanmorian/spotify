import sys

input = sys.stdin.read().strip().split('\n')

for l in input[1:]:
    r, s = l.split()
    print(''.join(i*int(r) for i in s))