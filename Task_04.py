def sort_list(list: list):
    x = len(list)
    if not list:
        return []
    elif x == 1:
        list.append(list[0])
        return list
    else:
        tMax = list.index(max(list))  # индекс макс
        nMax = max(list)  # Число макс
        tMin = list.index(min(list))  # индекс мин
        nMin = min(list)  # Число мин
        a = []  # для индексов макc
        b = []  # для индексов мин
        for i in range(x):
            if list[i] == nMax:
                a.append(i)
                a.sort()
            elif list[i] == nMin:
                b.append(i)
                b.sort()
        if len(a) == 1 and len(b) == 1:
            list[tMax], list[tMin] = list[tMin], list[tMax]
            list.append(nMin)
            return list
        elif len(b) > 1 and len(a) == 1:
            for i in b:
                list.pop(i)
                list.insert(i, nMax)
            list.pop(a[0])
            list.insert(a[0], nMin)
            list.append(nMin)
            return list

        elif len(a) > 1 and len(b) == 0:
            for i in a:
                list.pop(i)
                list.insert(i, nMin)
            list.pop(b[0])
            list.insert(b[0], nMax)
            list.append(nMin)
            return list


#print(sort_list([]))  # => []
#print(sort_list([2, 4, 6, 8]))  # => [8, 4, 6, 2, 2]
#print(sort_list([1]))  # => [1, 1]
#print(sort_list([1, 2, 1, 3]))  # => [3, 2, 3, 1, 1]
#print(sort_list([1, 2, 1, 3, 5, 1, 70]))  # => [70, 2, 70, 3, 5, 70, 1, 1]
