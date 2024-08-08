A, B = map(int, input().split())
n = [1]
cnt = 2

while len(n) < B:
    for _ in range(cnt):
        n.append(cnt)
    cnt += 1
    
print(sum(n[A-1:B]))