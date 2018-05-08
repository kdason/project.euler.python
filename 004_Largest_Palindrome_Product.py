"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers
is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""


def largest_palindrome_product(limit):
    l = []
    for i in range(limit, (limit + 1) // 10, -1):
        for j in range(i, (limit + 1) // 10, -1):
            product = i * j
            if str(product) == str(product)[::-1]:
                l.append(product)
                break
    return max(l)


print(largest_palindrome_product(999))
