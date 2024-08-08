import sys

n, b = map(int, sys.stdin.readline().strip().split())
digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

r = []

while n:
    r.append(digits[n%b])
    n = n//b
    
print("".join(r[::-1]))