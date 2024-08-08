import sys

word = sys.stdin.readline().strip()
total_time = 0

for char in word:
    if char <= 'C': total_time += 3
    elif char <= 'F': total_time += 4
    elif char <= 'I': total_time += 5
    elif char <= 'L': total_time += 6
    elif char <= 'O': total_time += 7
    elif char <= 'S': total_time += 8
    elif char <= 'V': total_time += 9
    else: total_time += 10

print(total_time)