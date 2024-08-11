import sys

print((lambda a, b: 'go' if len(a)>=len(b) else 'no')(*sys.stdin.read().strip().split('\n')))