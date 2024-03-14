#!/usr.bin/python3

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def generate_primes_up_to_n(n):
    primes = []
    for i in range(2, n + 1):
        if is_prime(i):
            primes.append(i)
    return primes

def isWinner(x, nums):
    # Input validation
    if not all(isinstance(n, int) and n >= 1 for n in nums):
        raise ValueError("All elements of nums must be positive integers")
    if not all(1 <= n <= 10000 for n in nums) or not (1 <= x <= 10000):
        raise ValueError("x and each element of nums must be between 1 and 10000")

    prime_numbers = generate_primes_up_to_n(max(nums))
    maria_wins = 0
    for n in nums:
        maria_moves = sum(n % prime == 0 for prime in prime_numbers)
        # If Maria has an even number of moves, she will lose
        if maria_moves % 2 == 0:
            continue
        else:
            maria_wins += 1

    if maria_wins > x - maria_wins:
        return "Maria"
    elif maria_wins < x - maria_wins:
        return "Ben"
    else:
        return None