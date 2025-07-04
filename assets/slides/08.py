# Lecture 08: Tree Recursion

def streak(n):
    """Return whether positive n is a dice integer in which all the digits are the same.

    >>> streak(22222)
    True
    >>> streak(4)
    True
    >>> streak(22322)  # 2 and 3 are different digits.
    False
    >>> streak(99999)  # 9 is not allowed in a dice integer.
    False
    """
    # Base case: single digit. Must be within [1, 6]
    if 1 <= n <= 6:
        return True
    elif n <= 9:
        return False
    # Recursive case.
    # Ex: 2222 is a streak if 222 is a streak AND RHS digit matches
    #   the LHS's digit.
    cur_rhs_digit = n % 10
    next_rhs_digit = (n // 10) % 10
    if cur_rhs_digit != next_rhs_digit:
        return False
    return streak(n // 10)
    # return streak(n // 10) and (cur_rhs_digit == next_rhs_digit)

########################################################################################
# BEGIN [Demo00]
########################################################################################
# Intent:
# - Additional recursion practice, via a fun game
# - I added the `verbose=True` kwarg to illustrate what the code is doing better
# - Feel free to share this VSCode window and walkthrough the function

"""
# from slide in lecture
# 5 players, first to say 18 wins! (player2 wins)
sevens(18, 5)

# turn-by-turn breakdown with added print calls
sevens(18, 5, verbose=True)
"""

def sevens(n, k, verbose=False):
    """Return the (clockwise) position of who says n among k players.

    >>> sevens(2, 5)
    2
    >>> sevens(6, 5)
    1
    >>> sevens(7, 5)
    2
    >>> sevens(8, 5)
    1
    >>> sevens(9, 5)
    5
    >>> sevens(18, 5)
    2
    """
    def f(i, who, direction):
        # i: current game counter value
        # who: active player
        # direction: +1: clockwise, -1 means counterclockwise
        if verbose:
            print(f"Active player: {who}, direction={direction}, i={i}")
        if i == n:
            if verbose:
                print(f"Winning player: {who}")
            return who
        if i % 7 == 0 or has_seven(i):
            if verbose:
                print(f"Reversing direction from {direction} to: {-direction}")
            direction = -direction
        # move to next player (according to direction)
        who = who + direction
        # if direction == 1:
        #     who = who + 1
        # else:
        #     who = who - 1
        # who = (who - 1 % k) + 1
        if who > k:
            who = 1
        if who < 1:
            who = k
        return f(i + 1, who, direction)
    return f(1, 1, 1)

def sevens_iter(n, k):
    """Return the (clockwise) position of who says n among k players.

    >>> sevens_iter(2, 5)
    2
    >>> sevens_iter(6, 5)
    1
    >>> sevens_iter(7, 5)
    2
    >>> sevens_iter(8, 5)
    1
    >>> sevens_iter(9, 5)
    5
    >>> sevens_iter(18, 5)
    2
    """
    i, who, direction = 1, 1, 1
    while i < n:
        if i % 7 == 0 or has_seven(i):
            direction = -direction
        who = who + direction
        if who > k:
            who = 1
        if who < 1:
            who = k
        i = i + 1
    return who

def has_seven(n):
    if n == 0:
        return False
    elif n % 10 == 7:
        return True
    else:
        return has_seven(n // 10)

########################################################################################
# END [Demo00]
########################################################################################

def smallest_factor(n):
    """Return the smallest divisor of n above 1.

    >>> smallest_factor(10)
    2
    >>> smallest_factor(45)
    3
    >>> smallest_factor(49)
    7
    """
    def smallest_divisor(k):
        "Return the smallest divisor of n above or equal to k."
        if n % k == 0:
            return k
        else:
            return smallest_divisor(k + 1)
    return smallest_divisor(2)

def unique_prime_factors(n):
    """Return the number of unique prime factors of n.

    >>> unique_prime_factors(51)  # 3 * 17
    2
    >>> unique_prime_factors(9)   # 3 * 3
    1
    >>> unique_prime_factors(576) # 2 * 2 * 2 * 2 * 2 * 2 * 3 * 3
    2
    """
    k = smallest_factor(n)
    def no_k(n):
        "Return the number of unique prime factors of n other than k."
        if n == 1:
            return 0
        elif n % k != 0:
            # (Case 1) return the number of unique prime factors of the remaijning term
            return unique_prime_factors(n)
        else:
            # (Case 2) n is still divisible by k: divide it out
            return no_k(n // k)
    return 1 + no_k(n)

print(unique_prime_factors(576))

def count_partitions(n, m):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif m == 0:
        return 0
    else:
        with_m = count_partitions(n-m, m)
        without_m = count_partitions(n, m-1)
        return with_m + without_m

print("count_partitions(6, 4)", count_partitions(6, 4))

def count_park(n):
    """Count the ways to park cars and motorcycles in n adjacent spots.
    >>> count_park(1)  # '.' or '%'
    2
    >>> count_park(2)  # '..', '.%', '%.', '%%', or '<>'
    5
    >>> count_park(4)  # some examples: '<><>', '.%%.', '%<>%', '%.<>'
    29
    """
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        return 2 * count_park(n-1) + count_park(n-2)
