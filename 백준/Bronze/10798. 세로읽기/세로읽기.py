import sys

r = dict()

for i in range(5):
    line = sys.stdin.readline().strip()
    for j in range(len(line)):
        if line[j]:
            if j not in r:
                r[j] = []
            r[j].append(line[j])

print(''.join(j for i in r.values() for j in i))