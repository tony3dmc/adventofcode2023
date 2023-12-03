import os

DEBUG_MODE = True
PUZZLE_INPUT = 'example.txt'

# Day X: <puzzle name>, Part 1
def main():
    lines = get_input('example.txt')


# Puzzle solution functions below


# Generic helper functions below
def get_input(filename):
    with open(filename, 'r') as file:
        return file.read().split()

def debug(message):
    if DEBUG_MODE:
        print(message)

# Call the main method only when running this script directly
if __name__ == "__main__":
    main()