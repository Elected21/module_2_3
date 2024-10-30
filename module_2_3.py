my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
x = 0
y = len(my_list)

while True:

    if x == y:
        break

    elif my_list[x] > 0 and my_list[x] != 0:
        print(my_list[x])
        x += 1

    else:
        x += 1
