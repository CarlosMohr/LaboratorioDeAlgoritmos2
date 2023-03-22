list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

list_multiplos = []
# print(f'{item} - {item % 2 == 0}, {item % 3 == 0}, {item % 5 == 0}')
for item in list:
    if (item % 2 == 0) or (item % 3 == 0) or (item % 5 == 0):
        list_multiplos.append(item)

print(f'\n> list_multiplos: {list_multiplos}')