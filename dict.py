dict = {1: 'apple', 2: 'bat', 3: 'cup'}
for key in dict.keys():
    if key == 3:
        del dict[key]
print(dict)
