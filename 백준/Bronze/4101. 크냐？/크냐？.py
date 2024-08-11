import sys

print('\n'.join('Yes' if eval('>'.join(line.split())) else "No" for line in sys.stdin.read().strip().split('\n')[:-1]))