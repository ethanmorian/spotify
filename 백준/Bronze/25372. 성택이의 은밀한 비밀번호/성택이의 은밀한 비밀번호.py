import sys

print('\n'.join('yes' if 6 <= len(i) <= 9 else 'no' for i in sys.stdin.read().strip().split('\n')[1:]))