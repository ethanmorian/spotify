import sys

input = sys.stdin.read().strip().split('\n')

scores = list(map(int, input[1].split()))

m = max(scores)

scores = [(s / m * 100) for s in scores]

print(sum(scores) / len(scores))
