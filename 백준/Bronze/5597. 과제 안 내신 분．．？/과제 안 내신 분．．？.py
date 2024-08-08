import sys

input_lines = sys.stdin.read().strip().split()

input_numbers = list(map(int, input_lines))

missing_numbers = [str(i) for i in range(1, 31) if i not in input_numbers]

print('\n'.join(missing_numbers))
