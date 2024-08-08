import sys

n, b = sys.stdin.readline().strip().split()
digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

r = 0
for char in n:
    r = r * int(b) + digits.index(char)
    
print(r)