## First System: The Data

# Initializing The Grid. A 7 x 6 grid where tokens can go

grid = [
    [],
    [],
    [],
    [],
    [],
    [],
    [],
]

## System 1.5: Printing The Grid

def print_grid():
    # Initialize Print Grid
    print_grid = [
        ['[ ]','[ ]','[ ]','[ ]','[ ]','[ ]', '[ ]'],
        ['[ ]','[ ]','[ ]','[ ]','[ ]','[ ]', '[ ]'],
        ['[ ]','[ ]','[ ]','[ ]','[ ]','[ ]', '[ ]'],
        ['[ ]','[ ]','[ ]','[ ]','[ ]','[ ]', '[ ]'],
        ['[ ]','[ ]','[ ]','[ ]','[ ]','[ ]', '[ ]'],
        ['[ ]','[ ]','[ ]','[ ]','[ ]','[ ]', '[ ]'],
    ]
    for i, column in enumerate(grid):
        for j, cell in enumerate(column):
            print_grid[j][i] = cell
    
    for row in reversed(print_grid):
        for cell in row:
            print(cell, end=' ')
        print()


# let's assume the input is valid, for now

def place_token(color, col):
    grid[col].append('[' + color + ']')


# Testing print_grid function

place_token('X', 0)
place_token('X', 0)
place_token('X', 0)
place_token('O', 2)

print_grid()