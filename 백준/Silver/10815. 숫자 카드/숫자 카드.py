import sys

input = sys.stdin.read
data = input().split("\n")

a = set(data[1].split())

results = []
for i in data[3].split():
    if i in a:
        results.append("1")
    else:
        results.append("0")

print(" ".join(results))