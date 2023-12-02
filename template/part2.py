import os

def get_input(filename):
    with open(filename, 'r') as file:
        return file.read().split()

# Main
lines = get_input('input.txt')

