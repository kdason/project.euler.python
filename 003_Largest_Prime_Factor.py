"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""


def get_largest_prime_factor(number):
    factor_set = set()

    # while the number is divisible by 2, store 2 as a factor and keep dividing by 2
    while number % 2 == 0:
        factor_set.add(2)
        number /= 2

    # start with 3 now... as long as the number is larger than the square of the factor, do as follows.
    # If the number is divisible by the factor, store the factor and divide the number.
    # Once the number cannot be divided by the factor, increment by 2 (to skip even numbers) and restart.
    factor = 3
    while factor**2 <= number:
        while number % factor == 0:
            factor_set.add(factor)
            number //= factor
        factor += 2

    # If the number is still greater than 2, store it as a prime factor.
    if number > 2:
        factor_set.add(number)

    return max(factor_set)


print(get_largest_prime_factor(600851475143))

