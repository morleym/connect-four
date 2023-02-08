## First System: The Data

# Initializing The Grid. A 7 x 6 grid where tokens can go

grid = [
    ['[ ]','[ ]','[ ]','[ ]','[ ]','[ ]'],
    ['[ ]','[ ]','[ ]','[ ]','[ ]','[ ]'],
    ['[ ]','[ ]','[ ]','[ ]','[ ]','[ ]'],
    ['[ ]','[ ]','[ ]','[ ]','[ ]','[ ]'],
    ['[ ]','[ ]','[ ]','[ ]','[ ]','[ ]'],
    ['[ ]','[ ]','[ ]','[ ]','[ ]','[ ]'],
    ['[ ]','[ ]','[ ]','[ ]','[ ]','[ ]'],
]

## System 1.5: Printing The Grid

def print_grid():
    # Initialize Print Grid
    print_grid = [
        ['','','','','','',''],
        ['','','','','','',''],
        ['','','','','','',''],
        ['','','','','','',''],
        ['','','','','','',''],
        ['','','','','','',''],
    ]
    for i, column in enumerate(grid):
        for j, cell in enumerate(column):
            print_grid[j][i] = cell
    
    for row in print_grid:
        for cell in row:
            print(cell, end=' ')
        print()



## Second System: Placing a token. Will only be called with 'black' or 'red' as the color param

def place_token(color, x, y):
    pass


# Testing print_grid function
print_grid()