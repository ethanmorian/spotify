import sys

def s(n):
    f = n // 5
    
    while f >= 0:
        r = n - (f * 5)
        if r % 3 == 0:
            t = r // 3
            return f + t
        f -= 1
    
    return -1

n = int(sys.stdin.readline())
print(s(n))