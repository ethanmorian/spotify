import sys

input = sys.stdin.readline

m, n = map(int, input().split())

def sieve_of_eratosthenes(start, end):
    if end < 2:
        return []

    is_prime = [True] * (end + 1)
    is_prime[0], is_prime[1] = False, False

    for i in range(2, int(end**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, end + 1, i):
                is_prime[j] = False

    prime_numbers = [i for i in range(start, end + 1) if is_prime[i]]
    return prime_numbers

for i in sieve_of_eratosthenes(m, n):
    print(i)