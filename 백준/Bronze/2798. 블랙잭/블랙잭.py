import sys
import itertools

input = sys.stdin.readline

_, m = map(int, input().split())

print(max([sum(n) for n in itertools.combinations(list(map(int, input().split())),3) if sum(n) <= m]))