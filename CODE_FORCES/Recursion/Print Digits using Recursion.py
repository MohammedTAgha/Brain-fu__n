# print(100//10)
# print(10%100)
#

def get_digits(number):
    if number < 10:
        # If the number is less than 10, it only has one digit, so we can return it as a string
        return str(number)
    else:
        # Get the last digit of the number by taking the remainder of the number divided by 10
        last_digit = number % 10

        # Call the function again with the number divided by 10 and add the last digit to the beginning of the result
        return get_digits(number // 10) + ' ' + str(last_digit)


# Test the function
i = int(input())
cases = []
for i in range(0, i):
    cases.append(int(input()))
for n in cases:
    print(get_digits(n))
