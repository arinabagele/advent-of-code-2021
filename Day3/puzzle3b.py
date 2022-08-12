# Reads entry data from file
input_data = []
with open('puzzle3_input.txt') as file:
    for line in file:
        input_data.append(line)


def more_characters(input_list, index):
    """
    Function counts are there more 0 or 1 or equal number of them in the items' defined position
    :param input_list: list for counting 1 and 0
    :param index: position
    :return: '0', '1' or 'e' (stands for equal number of 1 and 0)
    """
    counter_0 = 0
    counter_1 = 0
    for i in range(0, len(input_list)):
        if input_list[i][index] == '0':
            counter_0 += 1
        else:
            counter_1 += 1
    if counter_0 > counter_1:
        return '0'
    elif counter_0 < counter_1:
        return '1'
    else:
        return 'e'


def filtered_list(input_list, index, parameter):
    """
    Function returns list with 0 or 1 on the defined position
    :param input_list: (list of strings) list that should be filtered according to 'parameter' value
    :param index: (string) specifies position that should be filtered
    :param parameter: (string) defines filter parameter '0' or '1'
    :return: filtered list
    """
    return_list = []

    for i in range(len(input_list)):
        if input_list[i][index] == parameter:
            return_list.append(input_list[i])
    return return_list


# Calculates oxygen_rate
oxygen_rate = input_data
range_number = len(input_data[0])

for i in range(range_number):
    if len(oxygen_rate) == 1:
        break
    character = more_characters(oxygen_rate, i)
    if character == 'e':
        character = '1'
    oxygen_rate = filtered_list(oxygen_rate, i, character)

# Calculates CO2 rate
co2_rate = input_data
for i in range(range_number):
    if len(co2_rate) == 1:
        break
    character = more_characters(co2_rate, i)
    match character:
        case 'e':
            co2_rate = filtered_list(co2_rate, i, '0')
        case '1':
            co2_rate = filtered_list(co2_rate, i, '0')
        case '0':
            co2_rate = filtered_list(co2_rate, i, '1')

print('result: {}'.format(int(oxygen_rate[0], 2) * int(co2_rate[0], 2)))
