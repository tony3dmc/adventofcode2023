import os

def get_input(filename):
    with open('input.txt', 'r') as file:
        return file.read().split()

def perform_search(search, forwards=True):
    map = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    numbers = map.values()
    
    partial = ''
    if not forwards:
        search = search[::-1]
    
    for char in search:
        if forwards:
            partial += char
        else:
            partial = char + partial

        if char in numbers:
            return { "value": char, "partial": partial }
        
        for word in map:
            if forwards:
                test = partial[-len(word):]
            else:
                test = partial[:len(word)]
            
            if test == word:
                return { "value": map[word], "partial": partial }
        
    return { "value": False, "partial": "" }

def get_calibration_numbers(str):
    results = perform_search(str)
    found = results['value']

    str = str[len(results['partial']):]
    results = perform_search(str, False)

    if results['value']:
        return found + results['value']

    return found + found

lines = get_input('input.txt')

sum = 0
for line in lines:
    calibration_value = get_calibration_numbers(line)
    sum += int(calibration_value)

# 54530
print(sum)