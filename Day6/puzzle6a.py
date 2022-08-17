fishes = []
with open('puzzle6_input.txt', 'r') as file:
    fishes = [int(num) for num in (file.readline()).split(',')]

for day in range(80):
    for i in range(len(fishes)):
        if fishes[i] == 0:
            fishes[i] = 6
            fishes.append(8)
        else:
            fishes[i] -= 1

print('Number of fishes in 80 days : {}'.format(len(fishes)))
