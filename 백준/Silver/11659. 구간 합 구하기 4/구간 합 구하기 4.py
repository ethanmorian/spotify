import sys

input = sys.stdin.read().strip().split('\n')


array = list(map(int, input[1].split()))

prefix_sum = [0] * (len(array) + 1)
for idx in range(1, len(array) + 1):
    prefix_sum[idx] = prefix_sum[idx - 1] + array[idx - 1]

for lines in input[2:]:
    i, j = map(int, lines.split())
    print(prefix_sum[j] - prefix_sum[i - 1])