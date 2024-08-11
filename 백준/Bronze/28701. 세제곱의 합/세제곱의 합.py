import sys

print((lambda n: f'{n*(n+1)//2}\n{(n*(n+1)//2)**2}\n{(n*(n+1)//2)**2}')(int(sys.stdin.read().strip())))