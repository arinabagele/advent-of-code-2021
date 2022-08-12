# Reads entry data from file
input_data = []
with open('puzzle2_input.txt') as file:
    for line in file:
        input_data.append(line)


depth = 0
forward = 0
for i in range(len(input_data)):
    #Splits each line from entry list to the two values: dirrection and steps
    movement, units = input_data[i].split()
    match movement:
        case 'forward':
            forward = forward + int(units)
        case 'down':
            depth = depth + int(units)
        case _:
            depth = depth - int(units)
print('Result (depth*forward) : {}'.format(depth * forward))
