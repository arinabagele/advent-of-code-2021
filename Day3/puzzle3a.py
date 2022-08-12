# Reads entry data from file
input_data = []
with open('puzzle3_input.txt') as file:
    for line in file:
        input_data.append(line)

gamma_rate = ''
epsilon_rate = ''

l = len(input_data[0].strip())
for i in range(l):
    counter_1 = 0
    counter_0 = 0
    for j in range(len(input_data)):
        if input_data[j][i] == '0':
            counter_0 += 1
        else:
            counter_1 += 1

    if counter_0 > counter_1:
        gamma_rate = gamma_rate + '0'
        epsilon_rate = epsilon_rate + '1'
    else:
        epsilon_rate = epsilon_rate + '0'
        gamma_rate = gamma_rate + '1'

print('result (gamma rate * epsilon rate) in decimal: {} '.format(int(gamma_rate, 2) * int(epsilon_rate, 2)))
