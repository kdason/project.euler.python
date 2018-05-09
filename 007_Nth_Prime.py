"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?
"""


def nth_prime(n):
    list_of_primes = [2]
    nbr = 3
    while len(list_of_primes) < n:
        for item in list_of_primes:
            if nbr % item == 0:
                break
        else:
            list_of_primes.append(nbr)
        nbr += 2
    return list_of_primes[-1]


print(nth_prime(10001))