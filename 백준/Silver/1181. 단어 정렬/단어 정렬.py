import sys

input = sorted(set(sys.stdin.read().strip().split()[1:]), key=lambda s: (len(s), s))

for i in input:
    print(i)