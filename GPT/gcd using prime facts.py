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

def gcd(a, b):
    """Returns the greatest common divisor of the input integers"""
    # Find the prime factorization of each integer
    factors_a = prime_factorization(a)
    factors_b = prime_factorization(b)

    # Create a dictionary that contains the common factors and their minimum exponent
    common_factors = {}
    for p, e in factors_a.items():
        if p in factors_b:
            common_factors[p] = min(e, factors_b[p])

    # Calculate the GCD by multiplying the common factors together, each raised to the power of its corresponding exponent
    gcd = 1
    for p, e in common_factors.items():
        gcd *= p ** e

    return gcd

# Test the function
print(gcd(12, 18)) # Output should be 6