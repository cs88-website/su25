# Lecture 15

class Link:
    """A linked list with a first element and the rest."""
    empty = ()
    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest
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

class Song:
    def __init__(self, name, artist, length):
        self.name = name
        self.artist = artist
        self.length = length
    def __repr__(self):
        return f"Song({self.name},{self.artist},{self.length})"

def longest_song(album):
    if album == Link.empty:
        return None
    if album.rest == Link.empty:
        return album.first
    rest_longest = longest_song(album.rest)
    if album.first.length > rest_longest.length:
        return album.first
    else:
        return rest_longest

def longest_song_iter(album):
    if album == Link.empty:
        return None
    cur_link, cur_longest_song = album.rest, album.first
    while cur_link != Link.empty:
        if cur_link.first.length > cur_longest_song.length:
            cur_longest_song = cur_link.first
        cur_link = cur_link.rest
    return cur_longest_song

song1 = Song("Golden Slumbers", "The Beatles", 92)
song2 = Song("A Day In The Life", "The Beatles", 337)
album1 = Link(song1, Link(song2))

print(longest_song(album1))
print(longest_song_iter(album1))

def link_copy(lnk):
    if lnk == Link.empty:
        return lnk
    return Link(lnk.first, link_copy(lnk.rest))

def interleave(lnk1, lnk2):
    if lnk1 == Link.empty:
        return link_copy(lnk2)
    elif lnk2 == Link.empty:
        return link_copy(lnk1)
    else:
        out_rest = interleave(lnk1.rest, lnk2.rest)
        return Link(lnk1.first, Link(lnk2.first, out_rest))

lnk1 = Link(1, Link(2, Link(3)))
lnk2 = Link(4, Link(5))
out1 = interleave(lnk1, lnk2)
print(out1)

def interleave_mut(lnk1, lnk2):
    if lnk1 == Link.empty or lnk2 == Link.empty:
        return
    else:
        out_rest = interleave_mut(lnk1.rest, lnk2.rest)
        lnk1.rest = lnk2
        lnk2.rest = out_rest

lnk1 = Link(1, Link(2, Link(3)))
lnk2 = Link(4, Link(5))
interleave_mut(lnk1, lnk2)
print("interleave_mut:", out1)
