# While loops
def while_ex00():
    print(3)
    print(2)
    print(1)
    print("blast off!")

def while_ex01():
    i = 3
    while i > 0:
        print(i)
        i = i - 1  # shorthand: i -= 1
    print("blast off!")

########################################################################################
# BEGIN [Demo00]
########################################################################################
# Intent:
# - demonstrate an infinite loop, and how to kill it via CTRL+c

def while_ex02():
    i = 3
    while i > 0:
        print(i)
    print("blast off!")

########################################################################################
# END [Demo00]
########################################################################################

# Prime factorization

########################################################################################
# BEGIN [Demo01]
########################################################################################
# Intent:
# - show that the prime_factors and smallest_factors functions work
# - show how one might approach implementing a nontrivial function using new tools like
#   while loops, if-stmts, and helper functions

def prime_factors(n):
    """Print the prime factors of positive integer n
       in non-decreasing order.

    >>> prime_factors(8)
    2
    2
    2
    >>> prime_factors(9)
    3
    3
    >>> prime_factors(10)
    2
    5
    >>> prime_factors(11)
    11
    >>> prime_factors(12)
    2
    2
    3
    >>> prime_factors(858)
    2
    3
    11
    13
    """
    while n > 1:
        k = smallest_factor(n)
        print(k)
        # print(f"n={n}, k={k}, next will update n={n // k}")
        n = n // k

def smallest_factor(n):
    """Return the smallest factor of n greater than 1."""
    k = 2
    while n % k != 0:
        # print(f"{n} is not divisible by {k}, checking: {k+1} next")
        k = k + 1
    return k

########################################################################################
# END [Demo01]
########################################################################################
