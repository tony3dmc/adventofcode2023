import os

def get_input(filename):
    with open(filename, 'r') as file:
        return file.read().split()

def main():
    lines = get_input('example.txt')

if __name__ == "__main__":
    main()