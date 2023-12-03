import os

DEBUG_MODE = False
PUZZLE_INPUT = 'input.txt'

def get_input(filename):
    with open(filename, 'r') as file:
        return file.read().split()

def is_gear(char):
    if char == '*':
        return True
    return False

def debug(message):
    if DEBUG_MODE:
        print(message)

def main():
    schematic = get_input(PUZZLE_INPUT)

    parts_with_gears = {}
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

                # Scan around it for gears
                debug(f"Checking line numbers {x - 1} to {x + 1}")
                for i in range(x - 1, x + 2):
                    if i < 0 or i >= len(schematic):
                        continue

                    for j in range(y - len(part_number), y + 2):
                        if j < 0 or j >= len(line):
                            continue

                        debug(f"Checking location ({i},{j})")
                        debug(f"Checking location ({i},{j}) = {schematic[i][j]}")
                        
                        if is_gear(schematic[i][j]):
                            location = i, j
                            if location in parts_with_gears:
                                parts_with_gears[location].append(part_number)
                            else:
                                parts_with_gears[location] = [part_number]

    gear_ratio_sum = 0
    for location in parts_with_gears:
        part_numbers = parts_with_gears[location]
        if len(part_numbers) == 2:
            gear_ratio_sum += int(part_numbers[0]) * int(part_numbers[1])

    print("Total sum of gear ratios is ", gear_ratio_sum)

if __name__ == "__main__":
    main()