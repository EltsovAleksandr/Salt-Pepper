def connect_dicts(dict1, dict2):
    s1 = sum(dict1.values())
    s2 = sum(dict2.values())
    dict3 = dict()
    if s1 <= s2:
        for k, v in dict1.items():
            if v > 10:
                dict3[k] = v
        for k, v in dict2.items():
            if v > 10:
                dict3[k] = v
    else:
        for k, v in dict2.items():
            if v > 10:
                dict3[k] = v
        for k, v in dict1.items():
            if v > 10:
                dict3[k] = v

    dict3 = dict(sorted(dict3.items(), key=lambda val: val[1]))
    return dict3


assert connect_dicts({"a": 2, "b": 12}, {"c": 11, "e": 5}) == {"c": 11, "b": 12}
assert connect_dicts({"a": 13, "b": 9, "d": 11}, {"c": 12, "a": 15}) == {
    "d": 11,
    "c": 12,
    "a": 13,
}
assert connect_dicts({"a": 14, "b": 12}, {"c": 11, "a": 15}) == {
    "c": 11,
    "b": 12,
    "a": 15,
}
