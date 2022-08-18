import numpy as np

positions = []
with open('puzzle7_input.txt', 'r') as file:
    positions = [int(num) for num in (file.readline()).split(',')]

# Find average as start point for comparing distances
p = round(np.mean(positions))

sum1 = 0
sum2 = 0
sum3 = 0
position_steps = {}

while max(positions) >= p >= min(positions):
    sum1 = 0
    sum2 = 0
    sum3 = 0

    # finds number of steps to reach provided position, -1 and +1
    for i in positions:
        sum1 += abs(i - p)
        sum2 += abs(i - (p - 1))
        sum3 += abs(i - (p + 1))

    position_steps[p] = sum1
    position_steps[p - 1] = sum2
    position_steps[p + 1] = sum3

    # Found position with min number of steps
    if p == [p for p, s in position_steps.items() if s == min(position_steps.values())][0]:
        break
    # Chooses position from 3 presented with min sum of steps
    p = [p for p, s in position_steps.items() if s == min(position_steps.values())][0]

print('Optimal position: {} \nSum of steps to reach it: {}'.format(p, position_steps[p]))
