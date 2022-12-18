from itertools import permutations


def find_permutations(array):
    # Find all permutations of the array with length len(array)
    permutation_iterator = permutations(array, len(array))

    # Convert the iterator to a list and return it
    return list(permutation_iterator)


# Test the function
array = [1, 2, 3]
print(len(find_permutations(array)))
