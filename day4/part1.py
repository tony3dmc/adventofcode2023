import os

DEBUG_MODE = True
PUZZLE_INPUT = 'input.txt'

# Day 4: Scratchcards, Part 1
def main():
    lines = get_input(PUZZLE_INPUT)
    score = 0
    for line in lines:
        winners, mine = parse_input(line)
        matches = get_matches(winners, mine)
        if len(matches):
            score += 2 ** (len(matches) - 1)
    
    print("Total score for all scratchcards is", score)

# Puzzle solution functions below
def get_matches(winning_numbers, my_numbers):
    return set(winning_numbers).intersection(my_numbers)

def parse_input(line):
    parts = line.split(':')[1].split('|')
    return [
        parts[0].split(),
        parts[1].split()
    ]

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