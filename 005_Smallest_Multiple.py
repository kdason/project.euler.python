"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""


def is_divisible(number, limit):
    for i in range(1, limit + 1):
        if number % i != 0:
            return False
    return True


def get_smallest_multiple(limit):
    ans = limit
    while not is_divisible(ans, limit):
        ans += limit
    return ans


print(get_smallest_multiple(20))
