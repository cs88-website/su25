class Tree:
    """A tree has a label and a list of branches."""
    def __init__(self, label, branches=[]):
        self.label = label
        for branch in branches:
            assert isinstance(branch, Tree)
        self.branches = list(branches)

    def is_leaf(self):
        return not self.branches

    def __repr__(self):
        if self.is_leaf():
            return f"Tree({self.label})"
        out = f"Tree({self.label}, ["
        for child in self.branches[:-1]:
            out += f"{repr(child)}, "
        out += f"{repr(self.branches[-1])}])"
        return out

t1 = Tree(
    3,
    [
        Tree(1),
        Tree(
            2,
            [
                Tree(1),
                Tree(1),
            ]
        )
    ]
)
print(t1)

t2 = Tree(
    3,
    [
        Tree(4),
        Tree(
            5,
            [
                Tree(7),
                Tree(6)
            ]
        ),
        Tree(
            2,
            [Tree(1)]
        )
    ]
)

print(t2)

def count_leaves(t):
    """Count the leaves of a tree."""
    if t.is_leaf():
        return 1
    else:
        branch_counts = [count_leaves(b) for b in t.branches]
        return sum(branch_counts)

print(count_leaves(t1))

def increment_leaves(t):
    """Return a tree like t but with leaf labels incremented."""
    if t.is_leaf():
        return Tree(t.label + 1)
    else:
        bs = [increment_leaves(b) for b in t.branches]
        return Tree(t.label, bs)

print(increment_leaves(t1))

def increment(t):
    """Return a tree like t but with all labels incremented."""
    return Tree(t.label + 1, [increment(b) for b in t.branches])

print(increment(t1))

def count_paths(t, total):
    """Return the number of paths from the root to any node in tree t
    for which the labels along the path sum to total.
    >>> t = Tree(3, [Tree(-1), Tree(1, [Tree(2, [Tree(1)]), Tree(3)]), Tree(1, [Tree(-1)])])
    >>> count_paths(t, 3)
    2
    >>> count_paths(t, 4)
    2
    >>> count_paths(t, 5)
    0
    >>> count_paths(t, 6)
    1
    >>> count_paths(t, 7)
    2
    """
    if t.label == total:
        found = 1
    else:
        found = 0
    return found + sum([count_paths(b, total - t.label) for b in t.branches])

t = Tree(3, [Tree(-1), Tree(1, [Tree(2, [Tree(1)]), Tree(3)]), Tree(1, [Tree(-1)])])
print("count_paths(t, 3):", count_paths(t, 3))
print("count_paths(t, 4):", count_paths(t, 4))
print("count_paths(t, 5):", count_paths(t, 5))


def largest_label(t):
    """Return the largest label in tree t."""
    if t.is_leaf():
        return t.label
    else:
        return max([largest_label(b) for b in t.branches] + [t.label])

print("largest_label(t1):", largest_label(t1))

def above_root(t):
    """Print all the labels of t that are larger than the root label."""
    def process(u):
        if u.label > t.label:
            print(u.label)
        for b in u.branches:
            process(b)
    process(t)

print("above_root(t1)")
above_root(t1)
print("above_root(t2)")
above_root(t2)

# Alternate Tree implementation
def tree(label, branches=None):
    if not branches:
        branches = []
    for branch in branches:
        assert is_tree(branch)
    return [label] + list(branches)

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    return not branches(tree)

# Alt tree impl

t1_alt = tree(3, [tree(1),
          tree(2, [tree(1),
                   tree(1)])])

print("t1_alt", t1_alt)

def largest_label_alt(t):
    """Return the largest label in tree t."""
    if is_leaf(t):
        return label(t)
    else:
        return max([largest_label_alt(b) for b in branches(t)] + [label(t)])

print("largest_label_alt(t):", largest_label_alt(t1_alt))
