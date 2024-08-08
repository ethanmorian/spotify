Croatia = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

import sys

input = sys.stdin.read().strip()
result = 0

for i in Croatia:
    result += input.count(i)
    input = input.replace(i, '_')
        
print(result+len(input.replace('_', '')))