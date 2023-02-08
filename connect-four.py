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
    
    
    # print top column labels
    for i in range(7):
        print(' ' + str(i) + ' ', end=' ')
    print()
    
    for row in reversed(print_grid):
        for cell in row:
            print(cell, end=' ')
        print()
    
    # print bottom column labels
    for i in range(7):
        print(' ' + str(i) + ' ', end=' ')
    print()



def place_token(letter, col):
    grid[col].append('[' + letter + ']')


# let's scope out handling people writing letters instead of a number because python isn't nice about str/int interoperability

def player_input(player):
    valid_input = False
    col = -1
    while not valid_input:
        col = input(player + ", enter a column to place your next token in: ")
        col = int(col)
        if col < 0 or col > 6:
            print('Please enter a valid column number from 0 through 6')
            continue
        elif len(grid[col]) >= 6:
            print('That column is full. Please select a different column')
            continue
        valid_input = True
    if player == "Player 1":
        place_token('X', col)
    else:
        place_token('O', col)
    


def play_game():
    print('Welcome, Players')
    print('Player 1, you are X. Player 2, you are O')
    print_grid()
    player_input("Player 1")
    player_input("Player 2")
    print_grid()
# Testing

play_game()