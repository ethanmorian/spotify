h, m = map(int, input().split())
i = int(input())

total_minutes = m + i

h += total_minutes // 60
m = total_minutes % 60

if h >= 24:
    h -= 24

print(h, m)