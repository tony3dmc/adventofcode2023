import os

def get_input(filename):
    with open(filename, 'r') as file:
        return file.read().split("\n")

def calculate_maximums(str):
    game = {
        'id': int(str.split(':')[0][5:]),
        'red': 0,
        'green': 0,
        'blue': 0,
    }

    for round in str.split(': ')[1].split('; '):
        for draw in round.split(', '):
            count, colour = draw.split()
            count = int(count)
            if game[colour] < count:
                game[colour] = count

    return game

# Main
lines = get_input('input.txt')

maximums_limit = { 'red': 12, 'green': 13, 'blue': 14 }

sum = 0
for line in lines:
    game = calculate_maximums(line)
    print(game)
    possible_game = True
    for colour in maximums_limit:
        if game[colour] > maximums_limit[colour]:
            possible_game = False

    if possible_game:
        sum += game['id']

print("Sum of all possible game IDs is", sum)