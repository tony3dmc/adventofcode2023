import os
import math

DEBUG_MODE = True
PUZZLE_INPUT = 'input.txt'

# Day 6: Wait For It, Part 1
def main():
    lines = get_input(PUZZLE_INPUT)
    time, min_distance = process_input(lines)

    lower, upper = get_times(time, min_distance)

    # 34123437
    print("The number of winning times is", upper - lower + 1)

# Puzzle solution functions below
def get_times(time, distance):
    root = math.sqrt(time**2 - (4 * distance))

    lower = math.ceil((-time + root) / -2)
    upper = math.floor((-time - root) / -2)
    return lower, upper


def process_input(lines):
    time = int("".join(lines[0].split()[1:]))
    distance = int("".join(lines[1].split()[1:]))
    return time, distance

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