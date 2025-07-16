# Lecture 13: Attributes

def demos():
    """Demos.

    >>> b = Account('Ada')
    >>> f = b.deposit
    >>> f(5)
    5
    >>> f(25)
    30
    >>> b.balance
    30
    >>> a = Account('Alan')
    >>> [a.deposit(n) for n in range(10)]
    [0, 1, 3, 6, 10, 15, 21, 28, 36, 45]
    >>> m = map(a.deposit, range(10, 13))
    >>> next(m)
    55
    >>> a.balance
    55
    >>> next(m)
    66
    >>> next(m)
    78
    >>> a.balance
    78
    >>> d = {1: 10, 2: 5, 3: 15, 4: 8, 5: 4}
    >>> max(d.keys(), key=d.get)
    3
    """

class Town:
    """Waldo in town.

    >>> Town(1, 7).street[2]
    'Waldo'
    """
    def __init__(self, w, aldo):
        if aldo == 7:
            self.street = {self.f(w): 'Waldo'}

    def f(self, x):
        return x + 1


class Beach:
    """Waldo at the beach.

    >>> Beach().walk(0).wave(0)
    'Waldo'
    """
    def __init__(self):
        sand = ['Wal', 'do']
        self.dig = sand.pop

    def walk(self, x):
        self.wave = lambda y: self.dig(x) + self.dig(y)
        return self

class Account:
    """An account has a balance and a holder.
    All accounts share a common interest rate.

    >>> a = Account('John')
    >>> a.holder
    'John'
    >>> a.deposit(100)
    100
    >>> a.withdraw(90)
    10
    >>> a.withdraw(90)
    'Insufficient funds'
    >>> a.balance
    10
    >>> a.interest
    0.02
    >>> Account.interest
    0.02
    """
    interest = 0.02

    def __init__(self, account_holder):
        self.holder = account_holder
        self.balance = 0

    def deposit(self, amount):
        """Add amount to balance."""
        self.balance = self.balance + amount
        return self.balance

    def withdraw(self, amount):
        """Subtract amount from balance if funds are available."""
        if amount > self.balance:
            return 'Insufficient funds'
        self.balance = self.balance - amount
        return self.balance

class Place:
    """A Place has a name and can print_history of all places before it.

    >>> places = [Place(x*2) for x in range(10)]
    >>> places[4].print_history()
    8
    6
    4
    2
    0
    >>> places[6].print_history()
    12
    10
    8
    6
    4
    2
    0
    """
    last = None
    def __init__(self, n):
        self.name = n
        self.then = Place.last
        Place.last = self

    def print_history(self):
        print(self.name)
        if self.then is not None:
            self.then.print_history()

########################################################################################
# BEGIN [Demo00]
########################################################################################
# Intent:
# - show how, in theory, we can approximate OOP via functions

class Point:
    num_points = 0
    # Constructor
    def __init__(self, x, y):
        self.x, self.y = x, y  # instance vars
        Point.num_points += 1

    # Instance Methods
    def distance_l2(self, pt_other):
        # Returns the L2 distance between myself
        # (self) and `pt_other`.
        return ((self.x - pt_other.x) ** 2
                + (self.y - pt_other.y) ** 2) ** 0.5

# global var
POINT_CLASS_VARS = {
    "num_points": 0,
}
def point_constructor(x, y):
    POINT_CLASS_VARS["num_points"] += 1
    return {"x": x, "y": y}
def point_get_x(pt):
    return pt["x"]
def point_get_y(pt):
    return pt["y"]
def point_get_num_points():
    return POINT_CLASS_VARS["num_points"]
def point_distance_l2(pt_a, pt_b):
    return ((point_get_x(pt_a) - point_get_x("x")) ** 2 + (point_get_y(pt_a) - point_get_y(pt_b)) ** 2) ** 0.5

# this does technically work
pt1 = point_constructor(1, 2)
pt2 = point_constructor(3, 4)
point_distance_l2(pt1, pt2)

# but the abstraction is easy for an undisciplined programmer to sidestep:
# eg I can directly access pt["x"] if I wanted to, rather than using the
# provided `point_get_x()/point_get_y()` functions:
# (aka an "Abstraction Violation" from Project01 "Maps")
pt1["x"] - pt1["y"]
# and, I can even do very strange things like:
# - create a point object without going through the constructor
# - mess with point representation
pt3 = [3, 4]  # create a point without incrementing the class var (!)
pt4 = [4, 5, 6]  # invalid point representation!

# Instead, OOP provides a more explicit abstraction barrier:
pt1_obj = Point(1, 2)
pt2_obj = Point(3, 4)
# pt1_obj is an instance of the Point class where the only ways I can
# interact with it are via the Class definition (aka an interface/contract)
pt1_obj



########################################################################################
# END [Demo00]
########################################################################################
