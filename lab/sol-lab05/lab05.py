def fibonacci(n):
    """Return the nth fibonacci number.

    >>> fibonacci(11)
    89
    >>> fibonacci(5)
    5
    >>> fibonacci(0)
    0
    >>> fibonacci(1)
    1
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def paths(m, n):
    """Return the number of paths from one corner of an
    M by N grid to the opposite corner.

    >>> paths(2, 2)
    2
    >>> paths(5, 7)
    210
    >>> paths(117, 1)
    1
    >>> paths(1, 157)
    1
    """
    if m == 1 or n == 1:
        return 1
    return paths(m - 1, n) + paths(m, n - 1)
    # Base case: Look at the two visual examples given. Since the insect
    # can only move to the right or up, once it hits either the rightmost edge
    # or the upper edge, it has a single remaining path -- the insect has
    # no choice but to go straight up or straight right (respectively) at that point.
    # There is no way for it to backtrack by going left or down.


def partition(n):
    """Return the number of partitions of positive integer n.

    >>> partition(5)
    7
    >>> partition(10)
    42
    >>> partition(15)
    176
    >>> partition(20)
    627
    """
    return part_max(n, n)

def part_max(n, m):
    """Return the number of partitions of n using integers up to m.

    >>> part_max(5, 3)
    5
    """
    if n < 0 or m <= 0:
        return 0
    if n == 0:
        return 1
    return part_max(n-m, m) + part_max(n, m-1)

