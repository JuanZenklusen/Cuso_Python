

#1, 99, 2, 98, 3, 97, 4, 96, 5, 95


a=99
for i in range(1,6):
    if i == 5:
        print(f'{i}, {a}')
    else:
        print(f'{i}, {a}', end=", ")
    a=a-1