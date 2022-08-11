# Reads input data from file to the list []
list = []
with open('puzzle1_input.txt') as file:
    for line in file:
        list.append(int(line))


def count_incr(measurements):
    i = 0
    incr = 0
    decr = 0

    while i < (len(measurements) - 1):
        if measurements[i] < measurements[i + 1]:
            incr = incr + 1
        else:
            decr = decr + 1
        i = i + 1

    return incr


print('Increases: {}'.format(count_incr(list)))
