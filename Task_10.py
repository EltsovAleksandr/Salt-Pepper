def count_words(string):
    d = {}
    s1 = str()
    for i in string.lower():
        if i.isalpha() or i == " ":
            s1 += i
    for i in s1.split():
        try:
            d[i]
        except KeyError:
            d[i] = 1
        else:
            d[i] += 1

    return d

