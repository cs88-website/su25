def shuffle(s):
    """Return a shuffled list that interleaves the two halves of s.

    >>> shuffle(range(6))
    [0, 3, 1, 4, 2, 5]
    >>> letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    >>> shuffle(letters)
    ['a', 'e', 'b', 'f', 'c', 'g', 'd', 'h']
    >>> shuffle(shuffle(letters))
    ['a', 'c', 'e', 'g', 'b', 'd', 'f', 'h']
    >>> letters  # Original list should not be modified
    ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    """
    assert len(s) % 2 == 0, 'len(seq) must be even'
    half = len(s) // 2
    shuffled = []
    for i in range(half):
        shuffled.append(s[i])
        shuffled.append(s[half + i])
    return shuffled


def deep_map(f, s):
    """Replace all non-list elements x with f(x) in the nested list s.

    >>> six = [1, 2, [3, [4], 5], 6]
    >>> deep_map(lambda x: x * x, six)
    >>> six
    [1, 4, [9, [16], 25], 36]
    >>> # Check that you're not making new lists
    >>> s = [3, [1, [4, [1]]]]
    >>> s1 = s[1]
    >>> s2 = s1[1]
    >>> s3 = s2[1]
    >>> deep_map(lambda x: x + 1, s)
    >>> s
    [4, [2, [5, [2]]]]
    >>> s1 is s[1]
    True
    >>> s2 is s1[1]
    True
    >>> s3 is s2[1]
    True
    """
    for i in range(len(s)):
        if type(s[i]) == list:
            deep_map(f, s[i])
        else:
            s[i] = f(s[i])



def common_players(roster):
    """Returns a dictionary containing values along with a corresponding
    list of keys that had that value from the original dictionary.
    >>> full_roster = {
    ...     "bob": "Team A",
    ...     "barnum": "Team B",
    ...     "beatrice": "Team C",
    ...     "bernice": "Team B",
    ...     "ben": "Team D",
    ...     "belle": "Team A",
    ...     "bill": "Team B",
    ...     "bernie": "Team B",
    ...     "baxter": "Team A"
    ... }
    >>> player_dict = common_players(full_roster)
    >>> type(player_dict) == dict
    True
    >>> for key, val in sorted(player_dict.items()):
    ...     print(key, list(sorted(val)))
    Team A ['baxter', 'belle', 'bob']
    Team B ['barnum', 'bernice', 'bernie', 'bill']
    Team C ['beatrice']
    Team D ['ben']
    """
    result_dict = {}
    for player in roster:
        team = roster[player]
        if team in result_dict:
            result_dict[team] += [player]
        else:
            result_dict[team] = [player]
    return result_dict

