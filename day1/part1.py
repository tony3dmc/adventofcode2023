import os
import re

def get_input(filename):
    with open('input.txt', 'r') as file:
        return file.read().split()

def remove_text(str):
    return re.sub(r'\D', '', str)

lines = get_input('input.txt')

sum = 0
for line in lines:
    numbers = remove_text(line)
    calibration_value = numbers[0] + numbers[-1]
    sum += int(calibration_value)

print(sum)