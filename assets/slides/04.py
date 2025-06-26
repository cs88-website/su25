########################################################################################
# BEGIN [Demo00]
########################################################################################
# DRY: Don't Repeat Yourself
# Intent:
# - demonstrate a "bad" example of a function implementation (`same_length_v0()`), then show 
#   how to "fix" it via the use of helper function (`digits()`) and `same_length()`

def same_length_v0(a, b):
    """Return whether positive integers a and b have the same number of digits.

    >>> same_length_v0(50, 70)
    True
    >>> same_length_v0(50, 100)
    False
    >>> same_length_v0(1000, 100000)
    False
    """
    # Count number of digits of a
    a_digits = 0
    while a > 0:
        a = a // 10
        a_digits = a_digits + 1
    # Count number of digits of b
    b_digits = 0
    while b > 0:
        b = b // 10
        b_digits = b_digits + 1
    return a_digits == b_digits

def digits(a):
    """Counts the number of digits of input integer a.

    >>> digits(5)
    1
    >>> digits(100)
    3
    """
    a_digits = 0
    while a > 0:
        a = a // 10
        a_digits = a_digits + 1
    return a_digits

def same_length(a, b):
    """Return whether positive integers a and b have the same number of digits.

    >>> same_length(50, 70)
    True
    >>> same_length(50, 100)
    False
    >>> same_length(1000, 100000)
    False
    """
    return digits(a) == digits(b)

########################################################################################
# END [Demo00]
########################################################################################

def square(x):
    return x * x
def call_fn(fn, x):
    return fn(x)

def return_fn(fn):
    return fn

# summation

# without HOF's, have to define a separate function
def summation_a_identity(k_end):
    k = 1
    out_sum = 0
    while k <= k_end:
        out_sum += k
        k += 1
    return out_sum

def summation_b_cubed(k_end):
    k = 1
    out_sum = 0
    while k <= k_end:
        out_sum += k ** 3
        k += 1
    return out_sum

def summation_c_mystery_math(k_end):
    k = 1
    out_sum = 0
    while k <= k_end:
        out_sum += (8 / ((4 * k - 3) * (4 * k - 1)))
        k += 1
    return out_sum


# Higher-order function

def double(x):
    return 2 * x

def twice(f, x):
    """Apply f twice to x.

    >>> twice(double, 3)
    12
    """
    return f(f(x))

########################################################################################
# BEGIN [Demo01]
########################################################################################
# Nim (aka 21)
# Intent:
# - Demo a fun example of HOF's applied to games
# - first, we will show how the code works, then show a simple `two_strat()` demo

def play(strategy0, strategy1, goal=21):
    """Play twenty-one and return the index of the winner.
    
    A strategy is a one-argument function that, given the current game state (current total),
    returns the player's action (an integer: 1, 2, or 3)

    >>> play(two_strat, two_strat)
    1
    """
    n = 0
    who = 0  # Player 0 goes first
    while n < goal:
        if who == 0:
            n = n + strategy0(n)
            who = 1
        elif who == 1:
            n = n + strategy1(n)
            who = 0
    return who  # The player who didn't just add to n

# Constant strategies: always choose 1, 2, or 3
def one_strat(n):
    return 1

def two_strat(n):
    return 2

def three_strat(n):
    return 3

def demo_all_const_strats():
    """Try all combinations of constant strategies, and print who wins
    """
    const_strats = [one_strat, two_strat, three_strat]
    strat_names = ["one_strat", "two_strat", "three_strat"]
    i_p0 = 0
    # P0: iterate over all constant strategies
    while i_p0 < len(const_strats):
        const_strat_p0 = const_strats[i_p0]
        # P1: iterate over all constant strategies
        i_p1 = 0
        while i_p1 < len(const_strats):
            const_strat_p1 = const_strats[i_p1]
            winner = play(const_strat_p0, const_strat_p1)
            print(f"P0={strat_names[i_p0]}, P1={strat_names[i_p1]}: winner={winner}")
            i_p1 += 1
        i_p0 += 1

########################################################################################
# END [Demo01]
########################################################################################


########################################################################################
# BEGIN [Demo02]
########################################################################################
# HOF: returning functions
# Intent:
# - Quickly show an example of a function returning an inner function
# - In next lecture, we will cover Environment Diagrams for inner functions
# Local function definitions; returning functions

def make_adder(n):
    """Return a function that takes one argument K and returns K + N.

    >>> add_three = make_adder(3)
    >>> add_three(4)
    7
    """
    def adder(k):
        return k + n
    return adder


make_adder(2000)(25)

########################################################################################
# END [Demo02]
########################################################################################

def random_strategy(n):
    import random
    return random.randint(1, 3)

########################################################################################
# BEGIN [Demo03]
########################################################################################
# Nim: more HOF examples
# Intent:
# - Show how to utilize HOF's for more sophisticated Nim strategies
# - (for fun) show how to get user input via `input()` in `interactive_strat()`

def noisy_strat(who, s):
    """A strategy that prints its choices.

    >>> play(noisy_strat(0, two_strat), noisy_strat(1, two_strat))
    Player 0 added 2 to 0 to reach 2
    Player 1 added 2 to 2 to reach 4
    Player 0 added 2 to 4 to reach 6
    Player 1 added 2 to 6 to reach 8
    Player 0 added 2 to 8 to reach 10
    Player 1 added 2 to 10 to reach 12
    Player 0 added 2 to 12 to reach 14
    Player 1 added 2 to 14 to reach 16
    Player 0 added 2 to 16 to reach 18
    Player 1 added 2 to 18 to reach 20
    Player 0 added 2 to 20 to reach 22
    1
    """
    def strat(n):
        choice = s(n)
        print('Player', who, 'added', choice, 'to', n, 'to reach', choice + n)
        return choice
    return strat

def interactive_strat(n):
    choice = 0
    while choice < 1 or choice > 3:
        print('How much will you add to', n, '(1-3)?', end=' ')
        choice = int(input())
    return choice

# to play against the "computer", with you (the human) as P0
# play(interactive_strat, two_strat)

########################################################################################
# END [Demo03]
########################################################################################


def f1():
    def fn2():
        pass
    def fn3():
        pass
    return fn2, fn3

fn2_global, fn3_global = f1()

# from here

def f1():
    def fn2():
        pass
    def fn3():
        pass
    return fn2

fn2_global = f1()
