N, M = map(int, input().split())

baskets = list(range(N + 1))

for _ in range(M):
    i, j = map(int, input().split())
    baskets[i], baskets[j] = baskets[j], baskets[i]

print(" ".join(map(str, baskets[1:])))