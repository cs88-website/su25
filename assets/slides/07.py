# Lecture 07: Recursion

def fact(n):
    if n == 0 or n == 1:
        return n
    return fact(n - 1) * n

print(fact(5))

# Factorial (upward version)

def fact_k(n, acc):
    """Compute n factorial times k.

    >>> fact_k(5, 1)
    120
    >>> fact_k(5, 10)
    1200
    >>> fact_k(0, 10)
    10
    """
    if n == 0 or n == 1:
        return acc
    return fact_k(n - 1, acc * n)

print(fact_k(6, 1))

def add_up(k):
    """Add up k numbers after k repeated calls.

    >>> add_up(4)(10)(20)(30)(40)  # Add up 4 numbers: 10 + 20 + 30 + 40
    100
    """
    assert k > 0
    def f(n):
        if k == 1:
            return n
        else:
            return lambda t: add_up(k - 1)(n + t)
    return f

print(add_up(4)(10)(20)(30)(40))

def add_up_v2(k):
    """Add up k numbers after k repeated calls.

    >>> add_up_v2(4)(10)(20)(30)(40)  # Add up 4 numbers: 10 + 20 + 30 + 40
    100
    """
    assert k > 0
    def f(n):
        if k == 1:
            return n
        else:
            return lambda t: add_up_v2(k - 1)(t) + n
    return f

# print("add_up_v2:", add_up_v2(4)(10)(20)(30)(40))
print("add_up_v2:", add_up_v2(1)(10))

def print_sums(n):
    print(n)
    def next_sum(k):
        return print_sums(n+k)
    return next_sum

print(print_sums(1)(2)(3))

printer1 = print_sums(1)
printer2 = print_sums(1000)
printer1 = printer1(2)(3)

printer2 = printer2(9)
