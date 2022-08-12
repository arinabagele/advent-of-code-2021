# Function checks is this value presented on board
# If Yes, then replaces it with 'X'
# Returns was value on board or not and modified/or not matrix
def check_nmb_on_board(matrix, value):
    value_on_board = False

    for i in matrix:
        for number in i:
            if number == int(value):
                matrix[matrix.index(i)][i.index(int(value))] = 'X'
                value_on_board = True

    return value_on_board, matrix


# Function checks is there row of 'X's
# Returns True or False
def check_row_bingo(matrix):
    row_bingo = False
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 'X':
                row_bingo = True
            else:
                row_bingo = False
                break
        if row_bingo:
            break
    return row_bingo


# Function checks is there column of 'X's
# Returns True or False
def check_column_bingo(matrix):
    column_bingo = False
    for j in range(len(matrix[0])):
        for i in range(len(matrix)):
            if matrix[i][j] == 'X':
                column_bingo = True
            else:
                column_bingo = False
                break
        if column_bingo:
            break
    return column_bingo


input_matrices = []
with open('puzzle4_data.txt', 'r') as file:
    values = [int(num) for num in (file.readline()).split(',')]
    next(file)
    input_matrices = [[int(num) for num in line.split()] for line in file if len(line) > 1]

dict_matrices = {}
j = 0

# Creates dictionary with bingo boards
for i in range(int(len(input_matrices) / 5)):
    matrix = []
    matrix.append(input_matrices[j])
    matrix.append(input_matrices[j + 1])
    matrix.append(input_matrices[j + 2])
    matrix.append(input_matrices[j + 3])
    matrix.append(input_matrices[j + 4])

    dict_matrices.update({i: matrix})
    j += 5

last_value = None
win_sum = 0
last_won_board = []
boards_to_ignore = []
for v in values:

    for m in dict_matrices:
        if m in boards_to_ignore:
            continue

        found_value, upd_matrix = check_nmb_on_board(dict_matrices[m], v)
        if found_value:
            dict_matrices[m] = upd_matrix
            if check_row_bingo(dict_matrices[m]) or check_column_bingo(dict_matrices[m]):
                # If there is a bingo board,
                # last value is overrode, last_won_board is overrode
                # won board is added to ignore list
                last_value = v
                last_won_board = dict_matrices[m]
                boards_to_ignore.append(m)

# Sum of left numbers is calculated
for l in last_won_board:
    for n in l:
        if n != 'X':
            win_sum += n
            
print('Sum: {}, last value: {}, mult: {}'.format(win_sum, last_value, int(win_sum) * int(last_value)))
