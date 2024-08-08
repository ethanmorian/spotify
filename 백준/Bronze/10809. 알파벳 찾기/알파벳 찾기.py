import sys

s = sys.stdin.read().strip()

result = [-1] * 26

for i in range(26):
    position = s.find(chr(97 + i))
    result[i] = position

print(' '.join(map(str, result)))