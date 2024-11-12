from math import prod


def multiply_numbers(inputs=None):
    a = []
    if not inputs:
        return None
    for i in str(inputs):
        if i.isdigit():
            a.append(int(i))
    if a:
        return prod(a)
    else:
        return None


