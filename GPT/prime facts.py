def prime_factorization(n):
    """Returns a dictionary containing the prime factorization of the input integer"""
    factors = {}
    # Find the prime factors of n
    while n % 2 == 0:
        if 2 not in factors:
            factors[2] = 0
        factors[2] += 1
        n = n // 2

    # Check for other prime factors
    i = 3
    while i <= n ** 0.5:
        while n % i == 0:
            if i not in factors:
                factors[i] = 0
            factors[i] += 1
            n = n // i
        i += 2

    # If there are no more prime factors, n itself is prime
    if n > 2:
        factors[n] = 1

    return factors

def divisors(n):
    """Returns a list of the positive divisors of the input integer"""
    factors = prime_factorization(n)

    # Create a list of all the divisors by iterating through the dictionary and using the prime factors and exponents to generate all the possible combinations of factors
    divisors = [1]
    for p, e in factors.items():
        divisors += [p ** i for i in range(1, e + 1)]

    return divisors

# Test the function
print(prime_factorization(12))
print(divisors(12)) # Output should be [1, 2, 3, 4, 6, 12]