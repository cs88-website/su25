# Lecture 19: Efficiency

class CallCounter:
    def __init__(self):
        self.n = 0

    def count(self, f):
        def counted(n):
            self.n += 1
            return f(n)
        return counted

# Vanilla recursive fib (no memoization)
def fib_vanilla(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        print(f"fib_vanilla({n}): calling fib_vanilla({n-2}) and fib_vanilla({n-1})")
        return fib_vanilla(n-2) + fib_vanilla(n-1)

# Fib with memoization (no decorators)
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        print(f"fib({n}): calling fib({n-2}) and fib({n-1})")
        return fib(n-2) + fib(n-1)

def memo(f):
    cache = {}
    def memoized(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]
    return memoized

# Note: important to overwrite global `fib` to point to memoized fib, otherwise
# memoization only works for "toplevel calls", not for intermediate recursive calls
fib = memo(fib)

# Memoized fib with Python decorators
@memo
def memo_fib_dec(n):
    if n == 0 or n == 1:
        return n
    print(f"memo_fib_dec({n}): calling memo_fib_dec({n-2}) and memo_fib_dec({n-1})")
    return memo_fib_dec(n-2) + memo_fib_dec(n-1)


def fib_tree(n):
    """A Fibonacci tree.

    >>> print(fib_tree(4))
    3
      1
        0
        1
      2
        1
        1
          0
          1
    """
    if n == 0 or n == 1:
        return Tree(n)
    else:
        left = fib_tree(n-2)
        right = fib_tree(n-1)
        fib_n = left.label + right.label
        return Tree(fib_n, [left, right])


