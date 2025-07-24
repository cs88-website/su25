# Lecture 17: Iterators

########################################################################################
# BEGIN [Demo00]
########################################################################################
# Intent:
# - quick tuple demo
def tuple_demos():
    (3, 4, 5, 6)
    3, 4, 5, 6
    ()
    tuple()
    tuple([1, 2, 3])
    # tuple(2)
    (2,)
    (3, 4) + (5, 6)
    (3, 4, 5) * 2
    5 in (3, 4, 5)

    # {[1]: 2}
    {1: [2]}
    {(1, 2): 3}
    # {([1], 2): 3}
    {tuple([1, 2]): 3}

########################################################################################
# END [Demo00]
########################################################################################

########################################################################################
# BEGIN [Demo01]
########################################################################################
# Intent:
# - case study in adding Iterable interface to Link.
# - this first demo focuses on LinkIterator

class IteratorInterface:
    """An illustration of Python's Iterator interface"""
    def __next__(self):
        """Returns next item, or raise StopIteration if at end"""
        raise NotImplementedError("Override me!")

    def __iter__(self):
        """Return iter instance, often self"""
        return self

class IterableInterface:
    """An illustration of Python's Iterable interface"""
    def __iter__(self):
        """Return an Iterator."""
        raise NotImplementedError("Override me!")

    def __getitem__(self, key):
        # Support indexing, eg `thing[key]`
        raise NotImplementedError("Override me!")

class Link:
    """A linked list with a first element and the rest."""
    empty = ()
    def __init__(self, first, rest=empty):
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'

class LinkIterator(IteratorInterface):
    """Iterator over linked lists (`LinkIterable`)"""
    def __init__(self, lnk_start):
        # print("Calling LinkIterator.__init__()")
        self.lnk_start = lnk_start
        self.lnk_cur = self.lnk_start

    def __next__(self):
        # print("Calling LinkIterator.__next__()")
        if self.lnk_cur == Link.empty:
            raise StopIteration()
        out = self.lnk_cur
        self.lnk_cur = self.lnk_cur.rest
        return out

class LinkCyclicIterator(LinkIterator):
    def __next__(self):
        if self.lnk_cur == Link.empty:
            self.lnk_cur = self.lnk_start
        out = self.lnk_cur
        self.lnk_cur = self.lnk_cur.rest
        return out

lnk1 = Link(1, Link(2, Link('meow')))
lnk1_iterator = LinkIterator(lnk1)
next(lnk1_iterator)
next(lnk1_iterator)
next(lnk1_iterator)
# next(lnk1_iterator)  # raises StopIteration

########################################################################################
# END [Demo01]
########################################################################################

########################################################################################
# BEGIN [Demo02]
########################################################################################
# Intent:
# - case study in adding Iterable interface to Link.
# - this focuses on LinkIterable

class LinkIterable(IterableInterface):
    """Linked list that supports py Iterable interface"""
    empty = ()
    def __init__(self, first, rest=empty):
        self.first = first
        self.rest = rest

    def __iter__(self):
        # print("Calling LinkIterable.__iter__()")
        return LinkIterator(self)

    def __getitem__(self, i):
        # print(f"Calling LinkIterable.__getitem__() i={i}")
        if i == 0:
            return self.first
        else:
            return self.rest[i-1]

    def __len__(self):
        return 1 + len(self.rest)

    def __repr__(self):
        if self.rest:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'

# With vanilla Link class, I can't iterate through it via standard Python ways
lnk1 = Link(1, Link(2, Link('meow')))
"""
# This raises: TypeError: 'Link' object is not iterable
for lnk in lnk1:
    print(lnk1.first)
"""
# But, by implementing Python's iterator/iterable interfaces, I can!
lnk1_iterable = LinkIterable(2, LinkIterable(3, LinkIterable('meow')))
for lnk in lnk1_iterable:
    print(lnk.first)

# Under the hood, Python's for loop is doing something like this:
def for_loop_sim(some_iterable):
    some_iterator = iter(some_iterable)
    while True:
        try:
            thing = next(some_iterator)
        except StopIteration:
            print("Caught StopIteration, terminating for loop")
            return
        print(thing)  # process thing

for_loop_sim(lnk1_iterable)

########################################################################################
# END [Demo02]
########################################################################################

def list_mutation_demos():
    s = [2, [3, 4], 5]
    s.append([6, 7])
    s.extend([8, 9])
    t = []
    t.extend(s)
    u = list(s)

def iterator_demos():
    """Using iterators

    >>> s = [[1, 2], 3, 4, 5]
    >>> next(s)
    Traceback (most recent call last):
        ...
    TypeError: 'list' object is not an iterator
    >>> t = iter(s)
    >>> next(t)
    [1, 2]
    >>> next(t)
    3
    >>> u = iter(s)
    >>> next(u)
    [1, 2]
    >>> list(t)
    [4, 5]

    >>> a = [1, 2, 3]
    >>> b = [a, 4]
    >>> c = iter(a)
    >>> d = c
    >>> print(next(c))
    1
    >>> print(next(d))
    2
    >>> b
    [[1, 2, 3], 4]
    """

def average(s):
    """Return the average of values in a list.

    >>> average([3, 4, 5, 6])
    4.5
    >>> average(map(lambda x: x * x, [3, 4, 5, 6]))
    Traceback (most recent call last):
        ...
    ZeroDivisionError: division by zero
    """
    return sum(s) / len(list(s))

########################################################################################
# BEGIN [Demo03]
########################################################################################
# Intent: quick demo of `map` builtin function, and how it returns an iterator

def double(x):
    print('***', x, '=>', 2*x, '***')
    return 2*x

def map_demo():
    """Using built-in sequence functions.

    >>> bcd = ['b', 'c', 'd']
    >>> [x.upper() for x in bcd]
    ['B', 'C', 'D']
    >>> caps = map(lambda x: x.upper(), bcd)
    >>> next(caps)
    'B'
    >>> next(caps)
    'C'
    >>> s = range(3, 7)
    >>> doubled = map(double, s)
    >>> next(doubled)
    *** 3 => 6 ***
    6
    >>> next(doubled)
    *** 4 => 8 ***
    8
    >>> list(doubled)
    *** 5 => 10 ***
    *** 6 => 12 ***
    [10, 12]
    >>> all(map(double, range(-3, 3)))
    *** -3 => -6 ***
    *** -2 => -4 ***
    *** -1 => -2 ***
    *** 0 => 0 ***
    False
    """

########################################################################################
# END [Demo03]
########################################################################################
