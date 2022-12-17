# Find the number of zeros at the end of the decimal expansion of n !, where n is a positive
# integer.

def count_zeros(n):
    """Returns the number of zeros at the end of the decimal expansion of n!"""
    # Initialize the counter
    zeros = 0

    # Divide n by powers of 5 and add the result to the counter
    divisor = 5
    while n >= divisor:
        zeros += n // divisor
        divisor *= 5

    return zeros

# Test the function
print(count_zeros(10)) # Output should be 2
print(count_zeros(100)) # Output should be 24