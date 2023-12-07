import os

DEBUG_MODE = True
PUZZLE_INPUT = 'input.txt'

# Day 6: Wait For It, Part 1
def main():
    lines = get_input(PUZZLE_INPUT)
    races = process_input(lines)
    winner_sum = 1
    for race in races:
        time, min_distance = race
        winners = 0
        for speed in range(time):
            distance = calculate_distance(speed, time - speed)
            if distance > min_distance:
                winners += 1
        if winners:
            winner_sum *= winners

    print("The margin of error value is", winner_sum)

# Puzzle solution functions below
def calculate_distance(speed, time):
    return speed * time

def process_input(lines):
    times = [int(item) for item in lines[0].split()[1:]]
    distances = [int(item) for item in lines[1].split()[1:]]
    races = []
    for i in range(len(times)):
        races.append((times[i], distances[i]))
    
    return races

# Generic helper functions below
def get_input(filename):
    with open(filename, 'r') as file:
        return file.read().split("\n")

def debug(message):
    if DEBUG_MODE:
        print(message)

# Call the main method only when running this script directly
if __name__ == "__main__":
    main()