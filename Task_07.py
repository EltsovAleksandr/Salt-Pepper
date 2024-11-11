def combine_anagrams(words_array):
    a = []  # список сумм ASCII
    c = dict()
    for i in words_array:
        a.append(sum([ord(j) for j in i]))
    x = 0
    for i in a:
        try:
            c[i]
        except KeyError:
            c[i] = [words_array[x]]
            x += 1
        else:
            c[i].append(words_array[x])
            x += 1

    b = list(i for i in c.values())
    print(b)
