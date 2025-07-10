# Lecture 11: Mutability

def deep_copy(lst):
    if not lst:
        return []
    elif type(lst[0]) == list:
        return [deep_copy(lst[0])] + deep_copy(lst[1:])
    else:
        # lst[0] is a primitive object (eg int)
        return [lst[0]] + deep_copy(lst[1:])

def shallow_copy(lst):
    if not lst:
        return []
    else:
        return [lst[0]] + shallow_copy(lst[1:])

print(shallow_copy([1, 2, [3, 4]]))

def reverse_lst(lst):
    """Given an input list, reverse the list
    via direct modification ("in-place").
    >>> nums = [1, 2, 3, 4]
    >>> reverse_lst(nums)
    >>> nums
    [4, 3, 2, 1]
    """
    i1 = 0
    i2 = len(lst) - 1
    for i1 in range(len(lst) // 2):
        i2 = len(lst) - 1 - i1
        # i2 = -(i1 + 1)  # also works!
        tmp = lst[i1]
        lst[i1] = lst[i2]
        lst[i2] = tmp

nums = [1, 2, 3, 4, 5]
print("before reverse:", nums)
reverse_lst(nums)
print("after reverse:", nums)

nums2 = [1, 2, 3, 4]
print("before reverse:", nums2)
reverse_lst(nums2)
print("after reverse:", nums2)

def square_nums_mutate(nums):
    i = 0
    while i < len(nums):
        nums[i] = nums[i] ** 2
        i += 1

def square_nums_pure(nums):
    return [num ** 2 for num in nums]

def square_nums_alt(nums):
    out = []
    for num in nums:
        out.append(num ** 2)
    return out

nums1 = [1, 2, 3]
square_nums_mutate(nums1)
# nums1 is now: [1, 4, 9]
print("square_nums_mutate nums:", nums1)
nums1 = [1, 2, 3]
print("square_nums_pure:", square_nums_pure(nums1))
print("square_nums_alt:", square_nums_alt(nums1))

def sample_code_pure():
    request = get_request()
    request_proc = preprocess_request(request)

    response = process_request(request)
    return response

def reverse_lst_v2(lst):
    # slicing creates a new list
    return lst[::-1]

# from tree import *

def list_demos():
    s = [3, 3, 7, 9]
    u = s
    s[1] = 5
    s.append(11)

    t = [x+3 for x in s]
    for i in range(len(s)):
        s[i] = s[i] + 3

    [s[-(i+1)] for i in range(len(s))]
    for i in range(len(s)):
        s[i] = s[-(i+1)]

def sums(n, m):
    """Return lists that sum to n containing positive numbers up to m that
    have no adjacent repeats, for n > 0 and m > 0.

    >>> sums(5, 1)
    []
    >>> sums(5, 2)
    [[2, 1, 2]]
    >>> sums(5, 3)
    [[1, 3, 1], [2, 1, 2], [2, 3], [3, 2]]
    >>> sums(5, 5)
    [[1, 3, 1], [1, 4], [2, 1, 2], [2, 3], [3, 2], [4, 1], [5]]
    >>> sums(6, 3)
    [[1, 2, 1, 2], [1, 2, 3], [1, 3, 2], [2, 1, 2, 1], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    """
    result = []
    for k in range(1, min(m + 1, n)):
        for rest in sums(n-k, m):
            if rest[0] != k:
                result.append([k] + rest)
    if n <= m:
        result.append([n])
    return result

def sums_v2(n, m):
    if n <= 0:
        return []
    elif m <= 0:
        return []
    elif n == 1:
        return [[1]]
    with_m = sums_v2(n - m, m)
    without_m = sums_v2(n, m - 1)
    # print(f"with_m sums_v2({n-m}, {m}): {with_m}")
    # print(f"without_m sum_v2({n}, {m-1}): {without_m}")
    candidates = with_m
    out = []
    for cand in candidates:
        for i1 in range(len(cand) + 1):
            if i1 == 0:
                if cand[i1] != m:
                    out.append([m] + cand)
            elif i1 == len(cand):
                if cand[i1 - 1] != m:
                    out.append(cand + [m])
            else:
                # cand=[2, 3]
                if cand[i1 - 1] != m and cand[i1] != m:
                    out.append(cand[:i1] + [m] + cand[i1:])
    out = dedup_lst(out)
    out.extend(without_m)
    if n <= m:
        out.append([n])
    return out

def dedup_lst(lst):
    out = set()
    for thing in lst:
        out.add(tuple(thing))
    return [list(thing) for thing in out]

print("sums_v2(5, 1)", sums_v2(5, 1))
print("sums_v2(5, 2)", sums_v2(5, 2))
print("sums_v2(5, 3)", sums_v2(5, 3))
print("sums_v2(5, 5)", sums_v2(5, 5))
print("sums_v2(6, 3)", sums_v2(6, 3))

#print("sums_v2(2, 3)", sums_v2(2, 3))

def sums_demo():
    result = [[1], [2], [3]]
    for k in range(1, 4):
        for s in result:
            if s[-1] != k:
                s.append(k)
                result.append(s)
    print(result)

def identity_demos():
    a = [10]
    b = a
    a == b
    a is b
    a.extend([20, 30])
    a == b
    a is b

    a = [10]
    b = [10]
    a == b
    a is not b
    a.append(20)
    a != b

    s = [3, 5, 7]
    t = [9, 11]
    s.append(t)
    s.extend(t)
    t[1] = 13
    print(s)

    s = [2, 7, [1, 8]]
    t = s[2]
    t.append([2])
    e = s + t
    t[2].append(8)
    print(e)

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



