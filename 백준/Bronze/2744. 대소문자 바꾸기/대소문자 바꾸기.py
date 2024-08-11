import sys

print(''.join(i.lower() if i.isupper() else i.upper() for i in sys.stdin.read()))