import sys

input = sys.stdin.read().strip().split("\n")

for line in input[:-1]:
    a, b = map(int, line.split())
    if b % a == 0:
        print("factor")
    elif a % b == 0:
        print("multiple")
    else:
        print("neither")