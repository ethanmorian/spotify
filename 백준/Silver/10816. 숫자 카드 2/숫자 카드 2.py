import sys
from collections import Counter

A, B = sys.stdin.buffer.read().splitlines()[1::2]
A = A.split()
B = B.split()

A_counter = Counter(A)

print(" ".join(str(A_counter[x]) if x in A_counter else "0" for x in B))