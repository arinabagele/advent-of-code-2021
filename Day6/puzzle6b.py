fishes = []
with open('puzzle6_input.txt', 'r') as file:
    fishes = [int(num) for num in (file.readline()).split(',')]

state_of_fishes = [0 for i in range(9)]

for i in fishes:
    state_of_fishes[i] += 1

number_of_days = 256
for day in range(number_of_days):
    temp = state_of_fishes[0]

    for f in range(8):
        state_of_fishes[f] = state_of_fishes[f+1]
    state_of_fishes[6] += temp
    state_of_fishes[8] = temp


print(sum(state_of_fishes))
