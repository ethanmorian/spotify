import sys

print((lambda x, y: max(int(x[::-1]), int(y[::-1])))(*sys.stdin.read().strip().split()))