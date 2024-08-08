import sys

A, B = sys.stdin.buffer.read().splitlines()[1::2]
A = set(A.split())
B = B.split()
print("\n".join("1" if x in A else "0" for x in B))