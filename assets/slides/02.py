# Assignment

########################################################################################
# BEGIN [Demo00]
########################################################################################
# Intent:
# - show that one can assign functions to new names (pow vs max)
# - show that functions have their own scope that "shadows" global scope (`g(y)`)
def ex00():
    """
    # First, do this in Python interpreter.
    # THEN, show it step-by-step in Python Tutor (in next slide)
    >>> max(2, 10)
    10
    >>> pow(2, 10)
    1024
    >>> max = pow
    >>> pow(2, 10)
    1024
    >>> pow = max
    >>> pow(2, 10)  # tricky: is this 10, or 1024?
    1024
    >>> max = pow
    >>> pow(2, 10)
    1024
    """
    pass

########################################################################################
# END [Demo00]
########################################################################################

def g(y):
    x = 2 * y
    return x + 1

def ex01():
    """
    >>> def g(y):
    ...     x = 2 * y
    ...     return x + 1
    ... 
    >>> x = 2
    >>> g(x)
    5
    >>> g(3 * x) + 3
    16
    >>> x
    2
    >>> y = 3
    >>> g(y)
    7
    >>> y
    3
    """

# https://pythontutor.com/cp/composingprograms.html#code=def%20g%28y%29%3A%0A%20%20%20%20x%20%3D%202%20*%20y%0A%20%20%20%20return%20x%20%2B%201%0A%20%20%20%20%0Ax%20%3D%202%0Aprint%28g%28x%29%29%0Aprint%28g%283%20*%20x%29%20%2B%203%29%0A&cumulative=true&curInstr=0&mode=display&origin=composingprograms.js&py=3&rawInputLstJSON=%5B%5D

# Name conflicts

from operator import mul

def square(square):
    return mul(square, square)
square(3)

# https://pythontutor.com/cp/composingprograms.html#code=from%20operator%20import%20mul%0Adef%20square%28square%29%3A%0A%20%20%20%20return%20mul%28square,%20square%29%0Aprint%28square%283%29%29&cumulative=true&curInstr=0&mode=display&origin=composingprograms.js&py=3&rawInputLstJSON=%5B%5D

# Multiple Assignment

def diff(x, y):
    """
    >>> def diff(x, y):
    ...     x, y = y, x
    ...     return y - x
    
    >>> x, y = 6, 1
    >>> x, y = y, x-y
    >>> diff(y, x)
    4
    """
    x, y = y, x
    return y - x
    
# https://pythontutor.com/cp/composingprograms.html#code=def%20diff%28x,%20y%29%3A%0A%20%20%20%20x,%20y%20%3D%20y,%20x%0A%20%20%20%20return%20y%20-%20x%0A%20%20%20%20%0Ax,%20y%20%3D%206,%201%0Ax,%20y%20%3D%20y,%20x-y%0Aprint%28diff%28y,%20x%29%29&cumulative=true&curInstr=0&mode=display&origin=composingprograms.js&py=3&rawInputLstJSON=%5B%5D

########################################################################################
# BEGIN [Demo01]
########################################################################################
# Intent:
# - demonstrate how print() returns None
# - demonstrate functions that return a value vs not return a value
# Print and None

def fn1(x):
    return x + 1 # versus print(x)

def fn2(x):
    # Hint: a function with no return value has an implicit `return None`
    print(x + 1)

def fn3(x):
    return print(x + 1)

def demo_01a():
    """
    # At first glance, all three functions do the same thing
    >>> fn1(42)
    43
    >>> fn2(42)
    43
    >>> fn3(42)
    43

    # However, this is deceptive: if we dig deeper and look at the return values,
    # we'll see the difference
    >>> out1 = fn1(42)
    >>> out1
    43
    >>> out2 = fn2(42)
    43
    # Note: nothing gets output here, This is because Python omits None.
    # To double check that it is indeed None, I'll use the `is` operator
    >>> out2
    >>> out2 is None
    True
    >>> out3 = fn3(42)
    43
    >>> out3 is None
    True
    """

def noisy(x):
    """
    >>> noisy(noisy(2) + noisy(3))
    NOISY 2
    NOISY 3
    NOISY 7
    8
    """
    print('NOISY', x)
    return x + 1

def demo_01b():
    """
    # Finally, we'll demonstrate the order in which call expressions are evaluated.
    # QUESTION: what will the python interpreter output here?
    >>> noisy(noisy(2) + noisy(3))
    # ANSWER:
    NOISY 2
    NOISY 3
    NOISY 7
    8
    # Note that the operands are evaluated first: noisy(2) + noisy(3)
    # Each sub call (eg noisy(2)) also evaluates its operands (aka arguments), but in this
    # case the number `2` is easy to evaluate: it evaluates to itself
    """

########################################################################################
# BEGIN [Demo02]
########################################################################################
# Intent:
# - demonstrate a fun involved example of a brute-force search algorithm
# Smalls

def f(x):
    return x - 1
def g(x):
    return 2 * (x + 1)
def h(x, y):
    return int(str(x) + str(y))

class Number:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

    def calls(self):
        return 0

class Call:
    """A call expression."""
    def __init__(self, f, operands):
        self.f = f
        self.operands = operands
        self.value = f(*[e.value for e in operands])

    def __repr__(self):
        return f'{self.f.__name__}({",".join(map(str, self.operands))})'

    def calls(self):
        return 1 + sum(o.calls() for o in self.operands)

# Note: adapted for C88C SU25. Remove Generators as we don't cover it in C88C.
def smalls(n):
    if n == 0:
        return [Number(5)]
    else:
        results = []
        for operand in smalls(n-1):
            results.append(Call(f, [operand]))
            results.append(Call(g, [operand]))
        for k in range(n):
            for first in smalls(k):
                for second in smalls(n-k-1):
                    if first.value > 0 and second.value > 0:
                        results.append(Call(h, [first, second]))
        return results

"""
# cs61a generator-based approach
def smalls(n):
    if n == 0:
        yield Number(5)
    else:
        for operand in smalls(n-1):
            yield Call(f, [operand])
            yield Call(g, [operand])
        for k in range(n):
            for first in smalls(k):
                for second in smalls(n-k-1):
                    if first.value > 0 and second.value > 0:
                        yield Call(h, [first, second])
"""

def show_all(i=3):
    for e in smalls(i):
        print(e, '->', e.value)

def sol():
    for i in range(9):
        r = [e for e in smalls(i) if e.value == 2025]
        for e in r:
            print(e, '->', e.value, 'has', e.calls(), 'calls')
