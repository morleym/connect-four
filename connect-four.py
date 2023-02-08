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
    for j, cell in enumerate(grid[col]):
        if cell == '[ ]':
            grid[col][j] = '[' + letter + ']'
            break


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
        elif grid[col][5] != '[ ]':
            print('That column is full. Please select a different column')
            continue
        valid_input = True
    if player == "Player 1":
        place_token('X', col)
    else:
        place_token('O', col)
    
def is_game_over():

    # Check for wins in rows

    for j in range(6):
        counter = 0
        letter = grid[0][j]
        for i in range(7):
            if grid[i][j] == letter:
                counter += 1
                if counter == 4 and letter != '[ ]':
                    if letter == '[X]':
                        print("Player 1 Wins by HORIZONTAL!")
                        return True
                    else:
                        print("Player 2 Wins by HORIZONTAL!")
                        return True
            else:
                counter = 1
                letter = grid[i][j]

    # Check for wins in columns

    for i in range(7):
        counter = 0
        letter = grid[i][0]
        for j in range(6):
            if grid[i][j] == letter:
                counter += 1
                if counter == 4 and letter != '[ ]':
                    if letter == '[X]':
                        print("Player 1 Wins by VERTICAL!")
                        return True
                    else:
                        print("Player 2 Wins by VERTICAL!")
                        return True
            else:
                counter = 1
                letter = grid[i][j]

    # Check for wins in up-and-right diagonals
    up_right_diag_start_points = [
        [0, 2],
        [0, 1],
        [0, 0],
        [1, 0],
        [2, 0],
        [3, 0],
    ]

    for point in up_right_diag_start_points:
        i = point[0]
        j = point[1]
        counter = 0
        letter = grid[i][j]

        while i <= 6 and j <= 5:
            if grid[i][j] == letter:
                counter += 1
                if counter == 4 and letter != '[ ]':
                    if letter == '[X]':
                        print("Player 1 Wins by DIAGONAL!")
                        return True
                    else:
                        print("Player 2 Wins by DIAGONAL!")
                        return True
            else:
                counter = 1
                letter = grid[i][j]
            
            i += 1
            j += 1
    
    # Check the up-and-left diagonals
    up_left_diag_start_points = [
        [6, 2],
        [6, 1],
        [6, 0],
        [5, 0],
        [4, 0],
        [3, 0],
    ]

    for point in up_left_diag_start_points:
        i = point[0]
        j = point[1]
        counter = 0
        letter = grid[i][j]

        while i >= 0 and j <= 5:
            if grid[i][j] == letter:
                counter += 1
                if counter == 4 and letter != '[ ]':
                    if letter == '[X]':
                        print("Player 1 Wins by DIAGONAL!")
                        return True
                    else:
                        print("Player 2 Wins by DIAGONAL!")
                        return True
            else:
                counter = 1
                letter = grid[i][j]
            
            i -= 1
            j += 1


    # Check If Board is Full
    empty_spots = False
    for i in range(7):
        if grid[i][5] == '[ ]':
            empty_spots = True
            break
    if not empty_spots:
        print("The board is full and no one wins!")
        return True

def play_game():
    print('Welcome, Players')
    print('Player 1, you are X. Player 2, you are O')
    print_grid()

    while True:
        player_input("Player 1")
        print_grid()
        if is_game_over():
            break
        player_input("Player 2")
        print_grid()
        if is_game_over():
            break


# Run it baybeeee 
play_game()