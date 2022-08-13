import re

# Reads entry data from the file
# Removes -> and ,
# Leaves only qualified numbers
input_data = []
temp = []
with open('puzzle5_input.txt') as file:
    for line in file:
        temp = [int(i) for i in re.split('->|,', line)]
        if temp[0] == temp[2] or temp[1] == temp[3]:
            input_data.append(temp)

# Finds max number from provided and creates a defined size matrix
max_nmb = 0
for i in input_data:
    if max(i) > max_nmb:
        max_nmb = max(i)

matrix = [[0 for i in range(0, max_nmb+1)] for j in range(0, max_nmb+1)]


for line in range(0, len(input_data)):
    start_x = min(input_data[line][0], input_data[line][2])
    finish_x = max(input_data[line][0], input_data[line][2])
    start_y = min(input_data[line][1], input_data[line][3])
    finish_y = max(input_data[line][1], input_data[line][3])

    # indicates that matrix's rows will be changed (x-axis)
    if start_y == finish_y:
        for i in range(start_x, finish_x+1):
            matrix[start_y][i] += 1

    # indicates that matrix's 'columns' will be changed (y-axis)
    if start_x == finish_x:
        for i in range(start_y, finish_y+1):
            matrix[i][start_x] += 1

count = 0
# Counts how many coordinates were overlapped
for r in matrix:
    for x in r:
        if x>1:
            count +=1

print('Result: {}'.format(count))
