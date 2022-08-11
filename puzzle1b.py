# Reads entry data from file
input_data = []
with open('puzzle1_input.txt') as file:
    for line in file:
        input_data.append(int(line))

sum_list = []
# Calculates sum of 3 entries
for i in range(2, len(input_data)):
    sum_list.append(input_data[i] + input_data[i - 1] + input_data[i - 2])

# Counts increases
counter = 0
for i in range(1, len(sum_list)):
    if sum_list[i - 1] < sum_list[i]:
        counter += 1

print('The answer is: {}'.format(counter))
