import sys
import math

print((lambda a: math.ceil(a/5))(*map(int, sys.stdin.read().strip().split())))