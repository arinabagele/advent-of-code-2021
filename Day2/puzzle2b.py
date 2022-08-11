# Reads entry data from file
input_data = []
with open('puzzle2_input.txt') as file:
    for line in file:
        input_data.append(line)

# Calculates depth and forward
depth = 0
horizontal = 0
aim = 0
for i in range(len(input_data)):
    movement, units = input_data[i].split()

    # down X increases your aim by X units.
    # up X decreases your aim by X units.
    # forward X does two things:
    #  1. It increases your horizontal position by X units.
    #  2.It increases your depth by your aim multiplied by X.
    match movement:
        case 'down':
            aim = aim + int(units)
        case 'up':
            aim = aim - int(units)
        case 'forward':
            horizontal = horizontal + int(units)
            depth = depth + aim * int(units)

print('depth: ', depth, 'horizontal: ', horizontal, 'aim: ', aim)
print('result: ', depth * horizontal)
