import os

DEBUG_MODE = False
PUZZLE_INPUT = 'input.txt'

# Day 4: Scratchcards, Part 2
def main():
    lines = get_input(PUZZLE_INPUT)
    card_counts = {}
    for line in lines:
        id, winners, mine = parse_input(line)
        matches = get_matches(winners, mine)
        card_counts[id] = {
            'matches': len(matches),
            'copies': 1
        }
    
    total = 0
    pos = 1
    while pos <= len(card_counts):
        debug(f"Processing card {pos} with {card_counts[pos]['matches']} matches and {card_counts[pos]['copies']} copies")

        for search in range(card_counts[pos]['matches']):
            debug(f"  Adding {card_counts[pos]['copies']} extra copies of card {pos + search + 1}")
            card_counts[pos + search + 1]['copies'] += card_counts[pos]['copies']
        
        total += card_counts[pos]['copies']
        pos += 1

    print("Total number of scratchcards is", total)

# Puzzle solution functions below
def get_matches(winning_numbers, my_numbers):
    return set(winning_numbers).intersection(my_numbers)

def parse_input(line):
    id = int(line.split(':')[0].split()[1])
    parts = line.split(':')[1].split('|')
    return [
        id,
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