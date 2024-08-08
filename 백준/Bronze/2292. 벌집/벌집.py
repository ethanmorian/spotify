import sys

n = int(sys.stdin.readline().strip())
k = 0

while n > 1 + 6 * (k * k + k * 1) / 2:
    k += 1
    
print(k+1)