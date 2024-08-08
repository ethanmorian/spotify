import sys
from collections import Counter

input = sys.stdin.read()
_, b, c = input.strip().split('\n')
counter = Counter(b.split())
print(counter[c])