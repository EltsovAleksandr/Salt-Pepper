import itertools


def max_odd(array):
    a = [i for i in array if isinstance(i, (int, float))]
    b = list(itertools.chain(*[i for i in array if isinstance(i, (list, tuple, set))]))
    if a == []:
        return None
    elif len(b) > 0:
        c = [i for i in a if i % 2 != 0] + [i for i in b if i % 2 != 0]
        if c == []:
            return None
        else:
            return max(c)
    else:
        c = [i for i in a if i % 2 != 0]
        if c == []:
            return None
        else:
            return max(c)


#print(max_odd([1, 2, 3, 4, 4]))  # => 3
#print(max_odd([21.0, 2, 3, 4, 4]))  # => 21
#print(max_odd(["ololo", "fufufu"]))  # => None
#print(max_odd([2, 2, 4]))  # => None
#print(max_odd(["ololo", 2, 3, 4, [1, 2], None]))  # => 3
#print(max_odd([(21.0, 2), 3, 4, 44, 4]))  # => 21.00
#print(max_odd([2, 152, 200, [152, 998, 1, 4], (14, 18, 814)]))  # => 1
#print(max_odd(["ololo", 2, 3, 4, [1, 2, 52, 11], None]))  # => 11
