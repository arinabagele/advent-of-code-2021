import re

# Reads entry data from file
# Removes -> and ,
# Leaves only qualified numbers
input_data = []
temp = []
with open('puzzle5_input.txt') as file:
    for line in file:
        temp = [int(i) for i in re.split('->|,', line)]
        # Checks that coordinates located on the x or y axes or 45degree diagonal
        if temp[0] == temp[2] or temp[1] == temp[3] or abs(temp[0] - temp[2]) == abs(temp[1] - temp[3]):
            input_data.append(temp)


# Finds max number from provided and creates this size matrix
max_nmb = 0
for i in input_data:
    if max(i) > max_nmb:
        max_nmb = max(i)

matrix = [[0 for i in range(0, max_nmb + 1)] for j in range(0, max_nmb + 1)]


# Marks coordinates on matrix
# param: coordinates = [[x1, y1][x2, y2]]
def mark_coordinates(mx, coordinates):
    start_x = coordinates[0][0]
    finish_x = coordinates[1][0]
    start_y = coordinates[0][1]
    finish_y = coordinates[1][1]

    # indicates that matrix's rows will be changed (x-axis)
    if start_y == finish_y:

        for i in range(min(start_x, finish_x), max(start_x, finish_x) + 1):
            mx[start_y][i] += 1

    # indicates that matrix's 'columns' will be changed (y-axis)
    elif start_x == finish_x:
        for i in range(min(start_y, finish_y), max(start_y, finish_y) + 1):
            mx[i][start_x] += 1

    # From top-left  to bottom-right
    elif start_x < finish_x and start_y < finish_y:
        i = 0
        while i <= (finish_x - start_x):
            mx[start_y + i][start_x + i] += 1
            i += 1

    # From bottom-right to top-left
    elif start_x > finish_x and start_y > finish_y:
        i = 0
        while i <= (start_x-finish_x):
            mx[start_y - i][start_x - i] += 1
            i += 1

    # From top-right to bottom-left
    elif start_x > finish_x and start_y < finish_y:
        i = 0
        while i <= (start_x - finish_x):
            mx[start_y + i][start_x - i] += 1
            i += 1

    # From bottom-left to top-right
    elif start_x < finish_x and start_y > finish_y:
        i = 0
        while i <= (finish_x - start_x):
            mx[start_y - i][start_x + i] += 1
            i += 1
    return mx


for line in range(0, len(input_data)):
    xy = [[input_data[line][0], input_data[line][1]], [input_data[line][2], input_data[line][3]]]

    matrix = mark_coordinates(matrix, xy)

count = 0
# Counts how many coordinates were overlapped
for r in matrix:
    for x in r:
        if x > 1:
            count += 1

print('Result: {}'.format(count))
