import sys

input = sys.stdin.read()
lines = input.strip().split('\n')

for line in lines:
    if line:
        A, B = map(int, line.split())
        print(A + B)