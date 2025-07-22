# Lecture 16: Data Examples

class Link:
    """A linked list with a first element and the rest."""
    empty = ()
    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def append(self, lnk):
        last_lnk = get_last(self)
        last_lnk.rest = lnk

    def insert_start(self, val):
        self.rest = Link(val, rest=self.rest)

    def __getitem__(self, i):
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

def get_last(lnk):
    if lnk.rest == Link.empty:
        return lnk
    return get_last(lnk.rest)

# test append
lnk1 = Link(1, Link(2, Link(3)))
lnk1.append(Link(4, Link(5)))
print("append:", lnk1)

# test insert_start
lnk1 = Link(1, Link(2, Link(3)))
lnk1.insert_start(42)
print("insert_start:", lnk1)

class LinkWithTail(Link):
    def __init__(self, first, rest=Link.empty):
        super().__init__(first, rest)
        self.tail = get_last(self)

    def append(self, lnk):
        self.tail.rest = lnk
        self.tail = lnk

# test tail
print("test tail")
lnk1 = LinkWithTail(1, LinkWithTail(2, LinkWithTail(3)))
print("lnk1.tail:", lnk1.tail)
print("lnk1:", lnk1)

# test fast append
lnk1 = LinkWithTail(1, LinkWithTail(2, LinkWithTail(3)))
lnk1.append(LinkWithTail(4, LinkWithTail(5)))
print("fast append", lnk1)

class LinkedList:
    def __init__(self, lnk):
        self.head = lnk
        self.tail = get_last(lnk)

    def append(self, lnk):
        self.tail.rest = lnk
        self.tail = lnk

print("With LinkedList wrapper class")
lnk_lst = LinkedList(Link(1, Link(2, Link(3))))
lnk_lst.append(Link(4, Link(5)))
print(lnk_lst.head)
