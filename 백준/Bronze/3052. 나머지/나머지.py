import sys

# Read input and convert to integers
input_numbers = map(int, sys.stdin.read().strip().split())

# Apply modulo 42 and use a set to find unique remainders
unique_remainders = set(num % 42 for num in input_numbers)

# Print the number of unique remainders
print(len(unique_remainders))