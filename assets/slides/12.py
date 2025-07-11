# Lecture 12: Object-oriented programming (OOP)

########################################################################################
# BEGIN [Demo00]
########################################################################################
# Intent:
# - quickly demo a simple example of a class

# I will create a class that represents a Person. For now, I'll just model two aspects
# of people: their name, and their age.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def have_birthday(self):
        self.age += 1
        print("Happy birthday!", self.name, "is now:", self.age)
        return self.age

# I can create (instantiate) a Person object
paul = Person("paul", 83)
# I can access their data (attributes)
paul.name
paul.age
# I can call methods on them, via the dot operator
paul.have_birthday()

getattr

########################################################################################
# END [Demo00]
########################################################################################

########################################################################################
# BEGIN [Demo01]
########################################################################################
# Intent:
# - a longer demo with a more involved class: the Account

class Account:
    """An account has a balance and a holder.

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
    """
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

    def transfer(self, destination, amount):
        """
        >>> a = Account("John")
        >>> b = Account("George")
        >>> a.deposit(100)
        >>> a.transfer(b, 50)  # a transfer 50 to b
        """
        result = self.withdraw(amount)
        if type(result) == str:  # something went wrong
            return result
        else:
            destination.deposit(amount)
            return 'Transfer successful'


def transfer(source, destination, amount):
    """Transfer amount between two accounts.

    >>> john = Account('John')
    >>> jack = Account('Jack')
    >>> john.deposit(100)
    100
    >>> jack.deposit(100000)
    100000
    >>> transfer(jack, john, 1000)
    'Transfer successful'
    >>> john.balance
    1100
    >>> jack.balance
    99000
    >>> transfer(john, jack, 10000)
    'Insufficient funds'
    >>> transfer(john, jack, 10)
    'Transfer successful'
    >>> john.balance
    1090
    >>> jack.balance
    99010
    """
    result = source.withdraw(amount)
    if type(result) == str:  # something went wrong
        return result
    else:
        destination.deposit(amount)
        return 'Transfer successful'

class Scam:
    """A scam account has a balance and a holder.

    >>> a = Scam('John')
    >>> a.holder
    'John'
    >>> a.deposit(100)
    102.0
    >>> a.withdraw(90)
    'We apologize for the delay'
    >>> a.withdraw(90)
    'We apologize for the delay'
    >>> a.balance
    102.0
    """
    def __init__(self, account_holder):
        self.holder = account_holder
        self.balance = 0

    def deposit(self, amount):
        """Add amount +2% to balance."""
        self.balance = self.balance + amount * 1.02
        return self.balance

    def withdraw(self, amount):
        """Subtract amount from balance if funds are available."""
        return 'We apologize for the delay'

def create(names):
    """Creates a dictionary of accounts, each with an initial deposit of 5.

    >>> accounts = create(['Alice', 'Bob', 'Charlie'])
    >>> accounts['Alice'].holder
    'Alice'
    >>> accounts['Bob'].balance
    5
    >>> accounts['Charlie'].deposit(10)
    15
    """
    result = {name: Account(name) for name in names}
    for a in result.values():
        a.deposit(5)
    return result

########################################################################################
# END [Demo01]
########################################################################################

class Point:
    # Constructor
    def __init__(self, x, y):
        self.x = x  # instance vars
        self.y = y
    # Getters
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
    # Instance Methods
    def distance_l2(self, pt_other):
        # Returns the L2 distance between myself
        # (self) and `pt_other`.
        return ((self.x - pt_other.x) ** 2
                + (self.y - pt_other.y) ** 2) ** 0.5

pt1 = Point(1, 2)
pt2 = Point(3, 4)
print(pt1.distance_l2(pt2))


# constructor
def create_point(x, y, color):
    return {"x": x, "y": y, "color": color}

# selectors
def get_x(point):
    return point["x"]
def get_y(point):
    return point["y"]
def get_color(point):
    return point["color"]
