list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

list_pares = []

for item in list:
    if item %2 == 0:
        list_pares.append(item)
print(f'\n> list_pares: {list_pares}')