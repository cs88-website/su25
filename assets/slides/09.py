# Lecture 09: Sequences

# iterating through sequence
my_nums = [1, 2, 3]
for num in my_nums:
    print(num * 2)

my_nums = [1, 2, 3]
i = 0
while i < len(my_nums):
    print(my_nums[i] * 2)
    i += 1

# concatenation
nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
nums3 = nums1 + nums2
print(nums3)

# sequence contains
nums1 = [1, 2, 3, 4]
2 in nums1
5 not in nums1

# string sequence example
words = ['apple', 'ymca']
for word in words:
    for letter in word:
        # concatenate
        print(letter + '!')

# Lists practice

digits = [1, 8, 2, 8]
8 in digits
[1, 8] in digits
1 in digits and 8 in digits

for x in digits:
    print(100 * x)

def print_negatives(s):
    for d in s:
        d = -d
        print(d)
    print(s)

########################################################################################
# BEGIN [Demo00]
########################################################################################
# Intent:
# - demonstrate the range object
# Range practice

def range_practice():
    # observe that range(4) outputs `range(0, 4)`, it's a special type of object
    range(4)
    # to actually view the range elements ("materialize" the range), use the list constructor
    list(range(4))
    # range(4) with one arg has an implicit start=0. more generally, range(start, end),
    # note that `end` is exclusive, `start` is inclusive!
    range(-2, 2)
    list(range(-2, 2))
    # fun fact: python does not immediately materialize the range object, this returns immediately
    range(2, 10000000)  # 9 zeroes slows things down a lot
    # ...but this results in a noticeable since Python has to create 10M integers
    list(range(2, 10000000))

########################################################################################
# END [Demo00]
########################################################################################

def is_even(x):
    return x % 2 == 0

my_nums = [1, 2, 3, 4]
out = []
for num in my_nums:
    if is_even(num):
        out.append(num * 2)

print(out)

my_nums = [1, 2, 3]
out = [num * 2 for num in my_nums if is_even(num)]



# List comprehension practice

xs = range(-10, 11)
ys = [x*x - 2*x + 1 for x in xs]

xs_where_y_is_below_10 = [x for x in xs if x*x - 2*x + 1 < 10]
xs_where_y_is_below_10 = [xs[i] for i in range(len(xs)) if ys[i] < 10]
print("with list comp:", xs_where_y_is_below_10)

# for loop
xs_where_y_is_below_10 = []
for i in range(len(xs)):
    if ys[i] < 10:
        xs_where_y_is_below_10 += [xs[i]]
print("with for loop:", xs_where_y_is_below_10)

# while loop
i = 0
xs_where_y_is_below_10 = []
while i < len(xs):
    if ys[i] < 10:
        xs_where_y_is_below_10 += [xs[i]]
    i += 1
print("with while loop:", xs_where_y_is_below_10)

# Recursion

def sum_list(s):
    """Sum the elements of list s.

    >>> sum([2, 4, 1, 3])
    10
    """
    if len(s) == 0:
        return 0
    else:
        return s[0] + sum_list(s[1:])

def large(s, n):
    """Return the sublist of positive numbers s with the largest sum up to n.

    >>> large([4, 2, 5, 6, 7], 1)
    []
    >>> large([4, 2, 5, 6, 7], 3)
    [2]
    >>> large([4, 2, 5, 6, 7], 8)
    [2, 6]
    >>> large([4, 2, 5, 6, 7], 19)
    [4, 2, 6, 7]
    >>> large([4, 2, 5, 6, 7], 20)
    [2, 5, 6, 7]
    >>> large([4, 2, 5, 6, 7], 24)
    [4, 2, 5, 6, 7]
    """
    if s == []:
        return []
    elif s[0] > n:
        return large(s[1:], n)
    else:
        first = s[0]  # a number
        with_s0 = [first] + large(s[1:], n - first)
        without_s0 = large(s[1:], n)
        if sum_list(with_s0) > sum_list(without_s0):
            return with_s0
        else:
            return without_s0

out1 = large([94, 2, 5, 6, 7], 24)
print(out1, sum(out1))


def large_v2(s, n):
    """Return the sublist of positive numbers s with the largest sum up to n.

    >>> large_v2([4, 2, 5, 6, 7], 1)
    []
    >>> large_v2([4, 2, 5, 6, 7], 3)
    [2]
    >>> large_v2([4, 2, 5, 6, 7], 8)
    [2, 6]
    >>> large_v2([4, 2, 5, 6, 7], 19)
    [4, 2, 6, 7]
    >>> large_v2([4, 2, 5, 6, 7], 20)
    [2, 5, 6, 7]
    >>> large_v2([4, 2, 5, 6, 7], 24)
    [4, 2, 5, 6, 7]
    """
    # Alternate recursive implementation
    if s == []:
        return []
    elif n < 0:
        # s contains only positive integers, and it's
        # impossible to add pos ints to get a neg/zero int
        return []
    else:
        first = s[0]  # a number
        with_s0 = [first] + large_v2(s[1:], n - first)
        without_s0 = large_v2(s[1:], n)
        sum_with_s0 = sum_list(with_s0)
        sum_without_s0 = sum_list(without_s0)
        if sum_with_s0 > sum_without_s0 and sum_with_s0 <= n:
            return with_s0
        else:
            return without_s0

out1 = large_v2([94, 2, 5, 6, 7], 24)
print(out1, sum(out1))
print(large_v2([0, 0], 0))