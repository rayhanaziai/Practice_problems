"""Return count number of prime numbers, starting at 2.

For example::

    >>> primes(0)
    []

    >>> primes(1)
    [2]

    >>> primes(5)
    [2, 3, 5, 7, 11]

"""


def is_prime(n):
    if n < 3:
        return True

    for i in xrange(2, n):
        if n % i == 0:
            return False
    return True


def primes(count):
    """Return count number of prime numbers, starting at 2."""

    result_lst = []
    i = 2
    while len(result_lst) != count:
        if is_prime(i):
            result_lst.append(i)
        i += 1
    return result_lst


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. GREAT WORK!\n"
