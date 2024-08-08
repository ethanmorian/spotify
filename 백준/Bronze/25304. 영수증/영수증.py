a = int(input())
for i in range(int(input())):
    b, c= map(int, input().split())
    a -= b*c
print("Yes" if a == 0 else "No")