def update_dictionary(d, key, value):
    if key in d:
        d[key]+=[value]
    else:
        if key*2 not in d:
            d[key*2]=[value]
        else:
            d[key*2]+=[value]
    return

d = {}
print(update_dictionary(d, 1, -1))  # None
print(d)                            # {2: [-1]}
update_dictionary(d, 2, -2)
print(d)                            # {2: [-1, -2]}
update_dictionary(d, 1, -3)
print(d)                            # {2: [-1, -2, -3]}