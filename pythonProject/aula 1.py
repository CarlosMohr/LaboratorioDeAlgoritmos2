list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# list.reverse()
# print(f'\n> Reverse: {my_list}')

reverso_values = []
for index in range(len(list)):
    reverso_values.append(list[(index + 1) * -1])

print(f'\n> Reversed List: {reverso_values}')