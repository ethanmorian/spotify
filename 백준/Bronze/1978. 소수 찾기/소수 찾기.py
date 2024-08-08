def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

import sys
input = sys.stdin.read
data = input().split()

N = int(data[0])
numbers = list(map(int, data[1:]))

prime_count = sum(1 for num in numbers if is_prime(num))
print(prime_count)