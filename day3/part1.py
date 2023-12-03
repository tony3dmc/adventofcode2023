import os

DEBUG_MODE = False
PUZZLE_INPUT = 'input.txt'

def get_input(filename):
    with open(filename, 'r') as file:
        return file.read().split()

def is_symbol(char):
    if char.isdigit() or char == '.':
        return False
    return True

def debug(message):
    if DEBUG_MODE:
        print(message)

def main():
    schematic = get_input(PUZZLE_INPUT)

    part_sum = 0
    for x in range(len(schematic)):
        line = schematic[x]

        # New line, reset the part number
        part_number = ''
        for y in range(len(line)):
            char = schematic[x][y]

            # Build up the part number
            if char.isdigit():
                part_number += char
            else:
                part_number = ''

            try:
                next_char = schematic[x][y+1]
            except:
                next_char = ''
            
            # Is this the end of the part number?
            if len(part_number) and not next_char.isdigit():
                debug(f"Found possible part number {part_number} at ({x},{y})")

                # Scan around it for symbols
                found_symbol = False
                debug(f"Checking line numbers {x - 1} to {x + 1}")
                for i in range(x - 1, x + 2):
                    if i < 0 or i >= len(schematic):
                        continue

                    for j in range(y - len(part_number), y + 2):
                        if j < 0 or j >= len(line):
                            continue

                        debug(f"Checking location ({i},{j})")
                        debug(f"Checking location ({i},{j}) = {schematic[i][j]}")
                        if is_symbol(schematic[i][j]):
                            found_symbol = True
                if found_symbol:
                    part_sum += int(part_number)
                    debug(f"Found part number - {part_number}")
                else:
                    debug(f"Not a part number - {part_number}")

    print("Total sum of part numbers is", part_sum)

if __name__ == "__main__":
    main()