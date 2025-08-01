def box_pointer_example():
    def f(s):
        x = s[0]
        return [x]

    t = [3, [2+2, 5]]
    u = [f(t[1]), t]
    print(u)

def double_eights(s):
    """Return whether two consecutive items of list s are 8.

    >>> double_eights([1, 2, 8, 8])
    True
    >>> double_eights([8, 8, 0])
    True
    >>> double_eights([5, 3, 8, 8, 3, 5])
    True
    >>> double_eights([2, 8, 4, 6, 8, 2])
    False
    """
    for i in range(len(s)):
        if s[i] == 8 and s[i+1] == 8:
            return True
    return False

print(double_eights([5, 3, 8, 3, 8]))

def double_eights_rec(s):
    """Return whether two consecutive items of list s are 8.

    >>> double_eights_rec([1, 2, 8, 8])
    True
    >>> double_eights_rec([8, 8, 0])
    True
    >>> double_eights_rec([5, 3, 8, 8, 3, 5])
    True
    >>> double_eights_rec([2, 8, 4, 6, 8, 2])
    False
    """
    if s[:2] == [8, 8]:
        return True
    elif len(s) < 2:
        return False
    else:
        return double_eights_rec(s[1:])

min(range(10), key=lambda i: abs(50 ** 0.5 - i))
sum([2, 3, 4], sum([20, 30, 40]))
any([x > 10 for x in range(10)])


# Strings
def str_example():
    """
    >>> s = '3 * '
    >>> print(s + s + s + 10)
    Traceback (most recent call last):
        ...
    TypeError: can only concatenate str (not "int") to str
    >>> print(s + s + s + str(10))
    3 * 3 * 3 * 10
    >>> eval(s + s + s + str(10))
    270
    """


def park(n):
    """Return the ways to park cars and motorcycles in n adjacent spots.

    >>> park(1)
    ['%', '.']
    >>> park(2)
    ['%%', '%.', '.%', '..', '<>']
    >>> park(3)
    ['%%%', '%%.', '%.%', '%..', '%<>', '.%%', '.%.', '..%', '...', '.<>', '<>%', '<>.']
    >>> len(park(4))
    29
    """
    if n < 0:
        return []
    elif n == 0:
        return ['']
    else:
        return (['%'  + s for s in park(n-1)] +
                ['.'  + s for s in park(n-1)] +
                ['<>' + s for s in park(n-2)])



