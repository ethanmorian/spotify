import sys
import math

A, B, V = map(int, sys.stdin.readline().strip().split())

days = math.ceil((V - A) / (A - B)) + 1

print(days)