import os

DEBUG_MODE = False
PUZZLE_INPUT = 'input.txt'

# Day 5: If You Give A Seed A Fertilizer, Part 1
def main():
    lines = get_input(PUZZLE_INPUT)
    almanac = process_input(lines)
    locations = []
    for seed in almanac['seeds']:
        current_val = seed
        for map in almanac['maps']:
            for ranges in almanac['maps'][map]:
                target, source, length = ranges
                if current_val in range(source, source + length):
                    current_val = target + (current_val - source)
                    break
        locations.append(current_val)
        print(f"Seed {seed} ended up as location {current_val}")
    print(f"Minumum location was {min(locations)}")


# Puzzle solution functions below
def process_input(lines):
    almanac = { 'seeds': [], 'maps': {} }
    current_map = ''
    for line in lines:
        if line[0:6] == 'seeds:':
            almanac['seeds'] = [int(item) for item in line.split(': ')[1].split()]
        elif '-to-' in line:
            current_map = line.split()[0]
            almanac['maps'][current_map] = []
        elif line:        
            almanac['maps'][current_map].append([int(item) for item in line.split()])
    return almanac

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