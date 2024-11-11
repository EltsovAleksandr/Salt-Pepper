def coincidence(list=None, range=None):
    if list == None or range == None:
        return []
    a = [i for i in range]
    b = []
    for i in list:
        if (type(i) in (int, float)) and a[0] <= i <= a[-1]:
            b.append(i)
    return b


print(coincidence([1, 2, 3, 4, 5], range(3, 6)))
print(coincidence())  # => []
print(coincidence([None, 1, "foo", 4, 2, 2.5], range(1, 4)))  # => [1, 2, 2.5]
